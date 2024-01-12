# Library for float division
from __future__ import division

# Library used for scientific calculations (wolfram alpha in python)
import sympy as sy

# Library used for unit interconversions
import pint

# Library for graphs
import networkx as nx


class GraphSolver:
    """
    This class is used to solve the graph
    """

    # Initialization of the graph either through the
    # name of the model or though the saved object
    def __init__(self, JSONgraph=None, Trace=False, Debug=True):
        # create a registry object for calculations with units
        self.ureg = pint.UnitRegistry()
        # save initial json
        self.Gjson = JSONgraph
        # initialyse model with json graph
        self.G = self.dejsonify_graph(JSONgraph)
        self.G = self.PrepareGAfterImport(self.G)
        # set the global variables according to the input
        self.Initialysed_G_eq = False
        self.Trace = Trace
        self.Debug = Debug
        self.SymmetryCount = 0
        self.error = {}

    # convert graph from json to the networkx format
    def dejsonify_graph(self, json_graph):
        """Dejsonify a graph from the frontend to a networkx graph."""
        graph = nx.DiGraph()
        for node in json_graph["nodes"]:
            graph.add_node(int(node))
            for attribute in json_graph["nodes"][node]:
                graph.nodes[int(node)][attribute] = json_graph["nodes"][node][attribute]
        for edge in json_graph["edges"]:
            graph.add_edge(
                json_graph["edges"][edge]["origin"],
                json_graph["edges"][edge]["target"],
                weight=json_graph["edges"][edge]["weight"],
            )
            if "target-port" in json_graph["edges"][edge]:
                graph.edges[
                    json_graph["edges"][edge]["origin"],
                    json_graph["edges"][edge]["target"],
                ]["target-port"] = json_graph["edges"][edge]["target-port"]
        return graph

    def PrepareGAfterImport(self, Graph):
        """Prepare the graph after import from graphml"""
        # PowerGates to be corrected
        PGcontainer = []
        # Remaping to change node names from str to int
        Remaping = {}
        for i in range(len(Graph)):
            Remaping[str(i)] = i
        Graph = nx.relabel_nodes(Graph, Remaping)
        # Container for variable names
        VarNameContainer = []
        # Add the default atributes to the variable and
        # functionalyse the string atributes such as unit and SY_Var
        for i in Graph.nodes(data="type"):
            if i[1] == "PG":
                PGcontainer.append(i[0])
            if i[1] == "C":
                unit_text = Graph.nodes[i[0]]["unit"]
                if unit_text == "":
                    Graph.nodes[i[0]]["unit"] = self.ureg["dimensionless"]
                    base_unit_factor = 1
                else:
                    base_unit = 1 * self.ureg[unit_text].to_base_units()
                    base_unit_text = str(base_unit.units)
                    base_unit_factor = base_unit.magnitude
                    Graph.nodes[i[0]]["unit"] = 1 * self.ureg[base_unit_text]
                value = float(Graph.nodes[i[0]]["value"])
                Graph.nodes[i[0]]["value"] = value * base_unit_factor
            if i[1] == "V":
                unit_text = Graph.nodes[i[0]]["unit"]
                if unit_text == "":
                    Graph.nodes[i[0]]["unit"] = self.ureg["dimensionless"]
                    base_unit_factor = 1
                else:
                    base_unit = 1 * self.ureg[unit_text].to_base_units()
                    base_unit_text = str(base_unit.units)
                    base_unit_factor = base_unit.magnitude
                    Graph.nodes[i[0]]["unit"] = 1 * self.ureg[base_unit_text]
                if Graph.nodes[i[0]]["state"] == "known":
                    value = float(Graph.nodes[i[0]]["value"])
                    Graph.nodes[i[0]]["value"] = value * base_unit_factor
                    Graph.nodes[i[0]]["known"] = True
                if Graph.nodes[i[0]]["state"] == "solution":
                    value = float(Graph.nodes[i[0]]["value"])
                    Graph.nodes[i[0]]["ExpectedValue"] = value * base_unit_factor
                    Graph.nodes[i[0]]["known"] = False
                if Graph.nodes[i[0]]["state"] == "unknown":
                    Graph.nodes[i[0]]["known"] = False
                SY_Var_text = Graph.nodes[i[0]]["varName"]
                while SY_Var_text in VarNameContainer:
                    SY_Var_text += "*"
                Graph.nodes[i[0]]["SY_Var"] = sy.Symbol(SY_Var_text)
                VarNameContainer.append(SY_Var_text)
        return Graph

    def Check(self):
        """Check the graph for errors"""
        # Find all SOLUTION variables and equations
        VariablesToBeFound = {}
        EquationsToBeParsed = {}
        result = {"Solved": True}

        for i in self.G.nodes():
            if ("state" in self.G.nodes[i]) and (
                self.G.nodes[i]["state"] == "solution"
            ):
                VariablesToBeFound[i] = self.G.nodes[i]["value"]
            if "parsing" in self.G.nodes[i]:
                EquationsToBeParsed[i] = self.G.nodes[i]["parsing"]
        if self.Debug:
            print("Equations for parsing: ", EquationsToBeParsed)
            print("Variables for solution: ", VariablesToBeFound)

        # SOLVE GRAPH
        solution = self.OneShotSolution()

        # CHECK THE SOLUTION
        for i in VariablesToBeFound.keys():
            if self.G.nodes[i]["SY_Var"] not in solution.keys():
                result["Solved"] = False
                result["Error"] = {"Type": "Система уравнений составлена не верно"}
            elif float(solution[self.G.nodes[i]["SY_Var"]]) != float(
                VariablesToBeFound[i]
            ):
                if self.Debug:
                    print("Variable:", self.G.nodes[i]["SY_Var"])
                    print("Expected result:", float(VariablesToBeFound[i]))
                    print("Solution:", float(solution[self.G.nodes[i]["SY_Var"]]))
                result["Solved"] = False
                result["Error"] = {"Type": "Система уравнений составлена не верно"}
        for i in EquationsToBeParsed.keys():
            if result["Solved"]:
                parsing = str(self.Parse_Eq(i, Ignore_List=[])[0])
                # Remove white spaces
                parsing = "".join(parsing.split())
                if self.Debug:
                    print("Equation", i, "was expected to be ", EquationsToBeParsed[i])
                    print("Equation", i, "was parsed as", parsing)
                if self.error == {}:
                    if parsing != EquationsToBeParsed[i]:
                        result["Solved"] = False
                        result["Error"] = {
                            "Type": "Уравнение составлено не верно",
                            "Eq_ID": i,
                            "Expected_Parsing": EquationsToBeParsed[i],
                            "Calculated_Parsing": parsing,
                        }
                else:
                    result["Solved"] = False
                    result["Error"] = self.error
        return result

    def OneShotSolution(self):
        """Solve the graph using one shot solution"""
        equations = []
        unknowns = []
        for i, j in self.G.nodes(data="type"):
            if j == "E":
                equations.append(self.Parse_Eq(i)[0])
            if j == "V" and self.G.nodes[i]["state"] != "known":
                unknowns.append(self.G.nodes[i]["SY_Var"])
        solution = sy.solve(tuple(equations), tuple(unknowns))
        if self.Debug:
            print("Equations", tuple(equations))
            print("Unknowns", tuple(unknowns))
            print("Solution", solution)
        return solution

    def Parse_Eq(self, NodeNum, Ignore_List=[]):
        """
        RECURENT IMPLEMENTATION
        Parsing of the equation on the node number E_number (recurrent implementation)
        Instruction 1: Equation(equation node which is not a variable) = Sum (w_i * Equation_i),
        where i are the neighbours
        Instruction 2: Equation(known variable) is its value
        Instruction 3: Equation(not known variable) is the variable itself
        Instruction 4: Equation(Multiplication gate) = Product of w_i f_i,
        where i are the neighbours
        Instruction 5: Equation(Power gate) = w_1 f_1 ** (w_2 f_2),
        where 1 and 2 are the neighbours,
        number of the base is located in the power gate atribute 'base'
        Instruction 6: Equation(ABS gate) = abs(neighbour)
        Ignore list is the list of nodes that were inspected before (to stop the algorithm to go back)
        """
        Ignore_List.append(NodeNum)
        ConstantNodes = ["C", "I"]
        # If the node is a variable:
        if self.G.nodes[NodeNum]["type"] == "V":
            Symbolic_Eq = self.G.nodes[NodeNum]["SY_Var"]
            Unit = self.G.nodes[NodeNum]["unit"]
            if self.G.nodes[NodeNum]["known"] is False:
                Numeric_Eq = self.G.nodes[NodeNum]["SY_Var"]
                Symbolic_Repr = self.G.nodes[NodeNum]["SY_Var"]
            else:
                Numeric_Eq = self.G.nodes[NodeNum]["value"]
                Symbolic_Repr = self.G.nodes[NodeNum]["SY_Var"]
        # If the node is a constant:
        elif self.G.nodes[NodeNum]["type"] in ConstantNodes:
            Numeric_Eq = self.G.nodes[NodeNum]["value"]
            Symbolic_Eq = self.G.nodes[NodeNum]["value"]
            Symbolic_Repr = self.G.nodes[NodeNum]["value"]
            Unit = self.ureg["dimensionless"]
        # If the node is a sinus:
        elif self.G.nodes[NodeNum]["type"] == "SIN":
            for i in self.G.in_edges(NodeNum):
                for j in i:
                    if not (j in Ignore_List):
                        PartialEquation = self.Parse_Eq(j, Ignore_List)
                        Numeric_Eq = sy.sin(PartialEquation[0])
                        Symbolic_Eq = sy.sin(PartialEquation[1])
                        Symbolic_Repr = sy.sin(PartialEquation[2])
                        Unit = PartialEquation[3]
                        if str(Unit.units) != "dimensionless":
                            self.error = {
                                "Type": "Конфликт размерностей. Проверьте узел sin().",
                                "SIN_ID": NodeNum,
                            }
        # If the node is a cosinus:
        elif self.G.nodes[NodeNum]["type"] == "COS":
            for i in self.G.in_edges(NodeNum):
                for j in i:
                    if not (j in Ignore_List):
                        PartialEquation = self.Parse_Eq(j, Ignore_List)
                        Numeric_Eq = sy.cos(PartialEquation[0])
                        Symbolic_Eq = sy.cos(PartialEquation[1])
                        Symbolic_Repr = sy.cos(PartialEquation[2])
                        Unit = PartialEquation[3]
                        if str(Unit.units) != "dimensionless":
                            self.error = {
                                "Type": "Конфликт размерностей. Проверьте узел cos().",
                                "COS_ID": NodeNum,
                            }
        elif self.G.nodes[NodeNum]["type"] == "ABS":
            for i in self.G.in_edges(NodeNum):
                for j in i:
                    if not (j in Ignore_List):
                        PartialEquation = self.Parse_Eq(j, Ignore_List)
                        Numeric_Eq = abs(PartialEquation[0])
                        Symbolic_Eq = abs(PartialEquation[1])
                        Symbolic_Repr = abs(PartialEquation[2])
                        Unit = PartialEquation[3]
        # If the node is an equation:
        elif self.G.nodes[NodeNum]["type"] == "E":
            Numeric_Eq = 0
            Symbolic_Eq = 0
            Symbolic_Repr = 0
            MasterUnit = None
            if len(self.G.in_edges()) == 0:
                Unit = self.ureg["dimensionless"]
            else:
                for i in self.G.in_edges(NodeNum):
                    for j in i:
                        if not (j in Ignore_List):
                            Ignore_List = [NodeNum]
                            PartialEquation = self.Parse_Eq(j, Ignore_List)
                            Numeric_Eq += self.G.edges[i]["weight"] * PartialEquation[0]
                            Symbolic_Eq += (
                                self.G.edges[i]["weight"] * PartialEquation[1]
                            )
                            Symbolic_Repr += (
                                self.G.edges[i]["weight"] * PartialEquation[2]
                            )
                            Unit = PartialEquation[3]
                            if MasterUnit is None:
                                MasterUnit = Unit
                            elif Unit is not None:
                                if MasterUnit != Unit:
                                    self.error = {
                                        "Type": "Конфликт размерностей",
                                        "Eq_ID": NodeNum,
                                    }
        # If the node is a multiplication gate:
        elif self.G.nodes[NodeNum]["type"] == "MG":
            Numeric_Eq = 1
            Symbolic_Eq = 1
            Symbolic_Repr = 1
            Unit = self.ureg["dimensionless"]
            for j, i in self.G.in_edges(NodeNum):
                if not (j in Ignore_List):
                    PartialEquation = self.Parse_Eq(j, Ignore_List)
                    Numeric_Eq *= self.G.edges[j, i]["weight"] * PartialEquation[0]
                    Symbolic_Eq *= self.G.edges[j, i]["weight"] * PartialEquation[1]
                    Symbolic_Repr *= self.G.edges[j, i]["weight"] * PartialEquation[2]
                    LocalUnit = PartialEquation[3]
                    if (LocalUnit is not None) and (Unit is not None):
                        Unit *= LocalUnit
                    else:
                        Unit = None
        # If the node is a summation gate:
        elif self.G.nodes[NodeNum]["type"] == "SG":
            Numeric_Eq = 0
            Symbolic_Eq = 0
            Symbolic_Repr = 0
            MasterUnit = None
            for j, i in self.G.in_edges(NodeNum):
                if not (j in Ignore_List):
                    PartialEquation = self.Parse_Eq(j, Ignore_List)
                    Numeric_Eq += self.G.edges[j, i]["weight"] * PartialEquation[0]
                    Symbolic_Eq += self.G.edges[j, i]["weight"] * PartialEquation[1]
                    Symbolic_Repr += self.G.edges[j, i]["weight"] * PartialEquation[2]
                    Unit = PartialEquation[3]
                    if MasterUnit is None:
                        MasterUnit = Unit
                    elif Unit is not None:
                        if MasterUnit != Unit:
                            self.error = {
                                "Type": "Конфликт размерностей. Проверьте узел суммы.",
                                "SG_ID": NodeNum,
                            }
        # If the node is a power gate:
        elif self.G.nodes[NodeNum]["type"] == "PG":
            base = self.G.nodes[NodeNum]["base"]
            power = self.G.nodes[NodeNum]["power"]
            PartialEquationBase = self.Parse_Eq(base, Ignore_List)
            PartialEquationPower = self.Parse_Eq(power, Ignore_List)
            Numeric_Eq = (
                self.G.edges[base, NodeNum]["weight"] * PartialEquationBase[0]
            ) ** (self.G.edges[power, NodeNum]["weight"] * PartialEquationPower[0])
            Symbolic_Eq = (
                self.G.edges[base, NodeNum]["weight"] * PartialEquationBase[1]
            ) ** (self.G.edges[power, NodeNum]["weight"] * PartialEquationPower[1])
            Symbolic_Repr = (
                self.G.edges[base, NodeNum]["weight"] * PartialEquationBase[2]
            ) ** (self.G.edges[power, NodeNum]["weight"] * PartialEquationPower[2])
            # Check if power can be evaluated
            BaseUnit = PartialEquationBase[3]
            Power = self.G.edges[power, NodeNum]["weight"] * PartialEquationPower[0]
            if isinstance(Power, float) and (BaseUnit is not None):
                Unit = BaseUnit**Power
            else:
                Unit = None
        return Numeric_Eq, Symbolic_Eq, Symbolic_Repr, Unit
