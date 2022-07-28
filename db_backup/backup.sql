--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 14.4 (Ubuntu 14.4-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: bundles; Type: TABLE; Schema: public; Owner: physai_admin
--

CREATE TABLE public.bundles (
    id integer NOT NULL,
    title text NOT NULL,
    description text NOT NULL,
    level text NOT NULL,
    outline text NOT NULL
);


ALTER TABLE public.bundles OWNER TO physai_admin;

--
-- Name: bundles_id_seq; Type: SEQUENCE; Schema: public; Owner: physai_admin
--

CREATE SEQUENCE public.bundles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bundles_id_seq OWNER TO physai_admin;

--
-- Name: bundles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: physai_admin
--

ALTER SEQUENCE public.bundles_id_seq OWNED BY public.bundles.id;


--
-- Name: problem_skills; Type: TABLE; Schema: public; Owner: physai_admin
--

CREATE TABLE public.problem_skills (
    id integer NOT NULL,
    problem_id integer NOT NULL,
    skill_id integer NOT NULL
);


ALTER TABLE public.problem_skills OWNER TO physai_admin;

--
-- Name: problem_skills_id_seq; Type: SEQUENCE; Schema: public; Owner: physai_admin
--

CREATE SEQUENCE public.problem_skills_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.problem_skills_id_seq OWNER TO physai_admin;

--
-- Name: problem_skills_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: physai_admin
--

ALTER SEQUENCE public.problem_skills_id_seq OWNED BY public.problem_skills.id;


--
-- Name: problems; Type: TABLE; Schema: public; Owner: physai_admin
--

CREATE TABLE public.problems (
    id integer NOT NULL,
    bundle_id integer NOT NULL,
    text text NOT NULL,
    graph text NOT NULL,
    problem_number integer NOT NULL,
    logo text,
    access text NOT NULL,
    difficulty text NOT NULL
);


ALTER TABLE public.problems OWNER TO physai_admin;

--
-- Name: problems_id_seq; Type: SEQUENCE; Schema: public; Owner: physai_admin
--

CREATE SEQUENCE public.problems_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.problems_id_seq OWNER TO physai_admin;

--
-- Name: problems_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: physai_admin
--

ALTER SEQUENCE public.problems_id_seq OWNED BY public.problems.id;


--
-- Name: skills; Type: TABLE; Schema: public; Owner: physai_admin
--

CREATE TABLE public.skills (
    id integer NOT NULL,
    name text NOT NULL,
    graph text NOT NULL,
    front_graph text NOT NULL,
    equation text NOT NULL
);


ALTER TABLE public.skills OWNER TO physai_admin;

--
-- Name: skills_id_seq; Type: SEQUENCE; Schema: public; Owner: physai_admin
--

CREATE SEQUENCE public.skills_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.skills_id_seq OWNER TO physai_admin;

--
-- Name: skills_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: physai_admin
--

ALTER SEQUENCE public.skills_id_seq OWNED BY public.skills.id;


--
-- Name: user_progress; Type: TABLE; Schema: public; Owner: physai_admin
--

CREATE TABLE public.user_progress (
    id integer NOT NULL,
    user_id integer NOT NULL,
    bundle_id integer NOT NULL,
    progress integer NOT NULL
);


ALTER TABLE public.user_progress OWNER TO physai_admin;

--
-- Name: user_progress_id_seq; Type: SEQUENCE; Schema: public; Owner: physai_admin
--

CREATE SEQUENCE public.user_progress_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_progress_id_seq OWNER TO physai_admin;

--
-- Name: user_progress_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: physai_admin
--

ALTER SEQUENCE public.user_progress_id_seq OWNED BY public.user_progress.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: physai_admin
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username text NOT NULL,
    password text NOT NULL,
    access integer NOT NULL,
    email text NOT NULL,
    firstname text NOT NULL,
    lastname text NOT NULL,
    birthdate text NOT NULL,
    country text NOT NULL
);


ALTER TABLE public.users OWNER TO physai_admin;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: physai_admin
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO physai_admin;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: physai_admin
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: bundles id; Type: DEFAULT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.bundles ALTER COLUMN id SET DEFAULT nextval('public.bundles_id_seq'::regclass);


--
-- Name: problem_skills id; Type: DEFAULT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.problem_skills ALTER COLUMN id SET DEFAULT nextval('public.problem_skills_id_seq'::regclass);


--
-- Name: problems id; Type: DEFAULT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.problems ALTER COLUMN id SET DEFAULT nextval('public.problems_id_seq'::regclass);


--
-- Name: skills id; Type: DEFAULT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.skills ALTER COLUMN id SET DEFAULT nextval('public.skills_id_seq'::regclass);


--
-- Name: user_progress id; Type: DEFAULT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.user_progress ALTER COLUMN id SET DEFAULT nextval('public.user_progress_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: bundles; Type: TABLE DATA; Schema: public; Owner: physai_admin
--

COPY public.bundles (id, title, description, level, outline) FROM stdin;
1	Введение в ФизАй графы	После прохождения этого курса вы поймете, как виртуально решать физические задачи и создавать новые, не прикасаясь к ручке и бумаге. Этот курс поможет вам понять, что такое физические графики, как правильно их читать и составлять.	для всех	This course describes the key elements of Physics of Graphs such as:\n\n* node Equation\n* Folding node\n* Multiplication node\n* Exponentiation node\n\nand much more.
2	Кинематика	Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.	для всех	Этот курс включает в себя следующие темы:\n* тема 1:\n$$\nE = mc^2\n$$\n* тема 2\n$$\na = b^2 + c^2\n$$
\.


--
-- Data for Name: problem_skills; Type: TABLE DATA; Schema: public; Owner: physai_admin
--

COPY public.problem_skills (id, problem_id, skill_id) FROM stdin;
\.


--
-- Data for Name: problems; Type: TABLE DATA; Schema: public; Owner: physai_admin
--

COPY public.problems (id, bundle_id, text, graph, problem_number, logo, access, difficulty) FROM stdin;
1	1	Hello! In this tutorial you will learn how to use our graph editor and construct solution graphs. \n\nOn the right you can see a graph editor window with nodes. You are about to construct your first equation: \n$$\nx=0\n$$ \nIn order to do that you will need to connect a circle, which represents a variable x to the yellow square, that represents an equation. Hold SHIFT and draw a line connecting variable $$x$$ to the equation. Make sure that you start with a circle!\n\nOnce you are finished check your graph by pressing Check button on the top of the graph editor window..	{"edges": {}, "nodes": {"1": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "x", "xpos": 2, "ypos": 2}, "2": {"parsed": true, "parsing": "x", "type": "E", "xpos": 4, "ypos": 2}}}	1	\N	1	2
2	1	Now you will learn how to incorporate multiple variables into the equation.\n\nEvery variable that gets connected to the equation modifies it in a way that **the sum** of all incoming variables equals to zero. Now equation reads $$x=0$$. Modify it so that it reads: \n$$\nx + y + z = 0\n$$\nRemember, that edges always start at the variable and go to the equation.	{"edges": {"2": {"origin": 5, "target": 8, "weight": 1}}, "nodes": {"5": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "x", "xpos": 2, "ypos": 2}, "6": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "y", "xpos": 4, "ypos": 4}, "7": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "z", "xpos": 6, "ypos": 2}, "8": {"parsed": true, "parsing": "x+y+z", "type": "E", "xpos": 4, "ypos": 2}}}	2	\N	1	1
3	1	Remove the unnecessary edge so that the equation transforms to x + z = 0. For this use a new edge eraser tool.	{"edges": {"31": {"origin": 41, "target": 41111, "weight": 1}, "311": {"origin": 411, "target": 41111, "weight": 1}, "3111": {"origin": 4111, "target": 41111, "weight": 1}}, "nodes": {"41": {"type": "V", "xpos": 2, "ypos": 2, "varName": "x", "unit": "", "value": "", "state": "unknown"}, "411": {"type": "V", "xpos": 4, "ypos": 4, "varName": "y", "unit": "", "value": "", "state": "unknown"}, "4111": {"type": "V", "xpos": 6, "ypos": 2, "varName": "z", "unit": "", "value": "", "state": "unknown"}, "41111": {"type": "E", "xpos": 4, "ypos": 2, "parsed": true, "parsing": "x+z"}}}	3	\N	1	1
4	1	Before the variable enters the equation it can be modified. Modify existing graph x = 0 to sin(x) = 0 by disattaching x from equation, attaching x to SIN node and SIN node to equation respectively.	{"edges": {"11": {"origin": 31, "target": 3111, "weight": 1}}, "nodes": {"31": {"type": "V", "xpos": 2, "ypos": 2, "varName": "x", "unit": "", "value": "", "state": "unknown"}, "311": {"type": "SIN", "xpos": 4, "ypos": 4}, "3111": {"type": "E", "xpos": 6, "ypos": 2, "parsed": true, "parsing": "sin(x)"}}}	4	\N	1	1
5	1	Apply skills from the last problem to construct the equation sin(x) + cos(y) + abs(z) = 0. Do you remember that abs() is the absolute value function? Lastly, make sure to move the nodes around so that they do not bother each other.	{"edges": {"21": {"origin": 71, "target": 71111, "weight": 1}, "211": {"origin": 71111, "target": 71111111, "weight": 1}}, "nodes": {"71": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "x", "xpos": 2, "ypos": 2}, "711": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "y", "xpos": 2, "ypos": 3}, "7111": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "z", "xpos": 2, "ypos": 4}, "71111": {"type": "SIN", "xpos": 4, "ypos": 3}, "711111": {"type": "ABS", "xpos": 4, "ypos": 2}, "7111111": {"type": "COS", "xpos": 4, "ypos": 1}, "71111111": {"parsed": "in(x) + cos(y) + Abs(z)", "parsing": "sin(x)+cos(y)+Abs(z)", "type": "E", "xpos": 6, "ypos": 3}}}	5	\N	1	1
6	1	Variables also can be combined before they enter the equation. Go on and construct equation x*y = 0 by attaching x and y to the multiplication gate (yellow square with cross) and attaching the multiplication gate to the equation. You can imagine it like that, x and y variables are going inside of the multiplication gate and produce x*y term. Then this term is passed on to the equation..	{"edges": {}, "nodes": {"41": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "x", "xpos": 2, "ypos": 2}, "411": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "y", "xpos": 2, "ypos": 4}, "4111": {"type": "MG", "xpos": 3, "ypos": 3}, "41111": {"parsed": true, "parsing": "x*y", "type": "E", "xpos": 5, "ypos": 3}}}	6	\N	1	1
7	1	Just as variables can be multiplied, they can be summed up. Go on and modify the equation by adding (a+b) term. Connect both a and b variables to the summation gate (yellow square with plus inside). After this, connect the summation gate to the equation. Final equation should read x*y + (a+b) = 0	{"edges": {"31": {"origin": 71, "target": 711111, "weight": 1}, "311": {"origin": 711, "target": 711111, "weight": 1}, "3111": {"origin": 711111, "target": 71111111, "weight": 1}}, "nodes": {"71": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "x", "xpos": 2, "ypos": 2}, "711": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "y", "xpos": 2, "ypos": 4}, "7111": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "a", "xpos": 8, "ypos": 2}, "71111": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "b", "xpos": 8, "ypos": 4}, "711111": {"type": "MG", "xpos": 3, "ypos": 3}, "7111111": {"type": "SG", "xpos": 7, "ypos": 3}, "71111111": {"parsed": "x*y+a+b", "parsing": "a+b+x*y", "type": "E", "xpos": 5, "ypos": 3}}}	7	\N	1	1
8	1	Go on and correct the equation that reads now c*d=0 to (a+b) * c = 0 by attaching the (a+b) summation block to the multiplication gate and disattaching d from it.	{"edges": {"51": {"origin": 711, "target": 711111, "weight": 1}, "511": {"origin": 71, "target": 711111, "weight": 1}, "5111": {"origin": 71111, "target": 7111111, "weight": 1}, "51111": {"origin": 7111, "target": 7111111, "weight": 1}, "511111": {"origin": 7111111, "target": 71111111, "weight": 1}}, "nodes": {"71": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "a", "xpos": 6, "ypos": 1}, "711": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "b", "xpos": 2, "ypos": 1}, "7111": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "c", "xpos": 2, "ypos": 7}, "71111": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "d", "xpos": 2, "ypos": 3}, "711111": {"type": "SG", "xpos": 4, "ypos": 3}, "7111111": {"type": "MG", "xpos": 4, "ypos": 5}, "71111111": {"parsed": "(a+b)*c", "parsing": "c*(a+b)", "type": "E", "xpos": 7, "ypos": 5}}}	8	\N	1	1
9	1	A special one is a power gate, used for the exponentiation, e.g. a^b. Since it is important to differentiate between base (a) and exponent (b), you have to additionally indicate exponent (b). Go on, connect (a) and (b) to the power gate and then indicate (b) as an exponent with a purple indicator tool. For this, you have to start with a power gate and draw an edge to the exponent (b).	{"edges": {}, "nodes": {"41": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "b", "xpos": 2, "ypos": 2}, "411": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "a", "xpos": 2, "ypos": 4}, "4111": {"type": "PG", "xpos": 5, "ypos": 3}, "41111": {"type": "E", "xpos": 7, "ypos": 3, "parsed": true, "parsing": "a**b"}}}	9	\N	1	1
10	1	Go on and change the exponent from b to sin(b). By disattaching b from the exponent indicator, attaching the b variable to the sin filter and sin to the power gate. Do not forget to indicate that exponent comes from the sin filter.	{"edges": {"4": {"origin": 7, "target": 8, "weight": 1, "target-port": "power"}, "5": {"origin": 6, "target": 8, "weight": 1, "target-port": "base"}, "6": {"origin": 8, "target": 10, "weight": 1}}, "nodes": {"6": {"type": "V", "xpos": 2, "ypos": 5, "varName": "a", "unit": "", "value": "", "state": "unknown"}, "7": {"type": "V", "xpos": 2, "ypos": 3, "varName": "b", "unit": "", "value": "", "state": "unknown"}, "8": {"type": "PG", "xpos": 4, "ypos": 4, "power": 7, "base": 6}, "9": {"type": "SIN", "xpos": 4, "ypos": 2}, "10": {"type": "E", "xpos": 6, "ypos": 4, "parsed": true, "parsing": "a**sin(b)"}}}	10	\N	1	1
11	1	As a challenge go on and create an equation a^(b+c) = 0 from scratch. As a tip: start by attaching the power gate to the equation and then base and exponent to the power gate.	{"edges": {}, "nodes": {"7": {"type": "V", "xpos": 1, "ypos": 1, "varName": "a", "unit": "", "value": "", "state": "unknown"}, "8": {"type": "V", "xpos": 2, "ypos": 1, "varName": "b", "unit": "", "value": "", "state": "unknown"}, "9": {"type": "V", "xpos": 3, "ypos": 1, "varName": "c", "unit": "", "value": "", "state": "unknown"}, "10": {"type": "PG", "xpos": 1, "ypos": 2}, "11": {"type": "SG", "xpos": 2, "ypos": 2}, "12": {"type": "E", "xpos": 3, "ypos": 2, "parsed": true, "parsing": "a**(b+c)"}}}	11	\N	1	1
12	1	You might have asked yourself, how do we go about the minus sign? The answer is, we have a dedicated edge for that, a negative edge (see red negative edge tool in the toolbar). \n\nGo on and create -a = 0 equation by attaching a to the equation with negative edge.	{"edges": {}, "nodes": {"3": {"type": "V", "xpos": 3, "ypos": 4, "varName": "a", "unit": "", "value": "", "state": "unknown"}, "4": {"type": "E", "xpos": 5, "ypos": 4, "parsed": true, "parsing": "-a"}}}	12	\N	1	1
13	1	Now, why is it actually -a and not a? The answer is, the value that passed to the equation is first multiplied with edge weight. In case of the red edge the weight is -1 and in case of the green one it is +1. \n\nIn all following exercises we will ask you to connect everything on the left hand side of the equation with a negative edge and everything on the right hand side of the equation with a positive edge to the equation. \n\nNow, go on and construct the equation a = b.	{"edges": {"2": {"origin": 4, "target": 6, "weight": -1}}, "nodes": {"4": {"type": "V", "xpos": 3, "ypos": 4, "varName": "a", "unit": "", "value": "", "state": "unknown"}, "5": {"type": "V", "xpos": 7, "ypos": 4, "varName": "b", "unit": "", "value": "", "state": "unknown"}, "6": {"type": "E", "xpos": 5, "ypos": 4, "parsed": true, "parsing": "-a+b"}}}	13	\N	1	1
14	1	Modify the equation further to get to the a = b * c with help of the multiplication gate and variable c.	{"edges": {"3": {"origin": 6, "target": 9, "weight": -1}, "4": {"origin": 7, "target": 9, "weight": 1}}, "nodes": {"6": {"type": "V", "xpos": 3, "ypos": 4, "varName": "a", "unit": "", "value": "", "state": "unknown"}, "7": {"type": "V", "xpos": 7, "ypos": 4, "varName": "b", "unit": "", "value": "", "state": "unknown"}, "8": {"type": "V", "xpos": 5, "ypos": 1, "varName": "c", "unit": "", "value": "", "state": "unknown"}, "9": {"type": "E", "xpos": 5, "ypos": 3, "parsed": true, "parsing": "-a+b*c"}, "10": {"type": "MG", "xpos": 5, "ypos": 2}}}	14	\N	1	1
15	1	Now we are finished with the introduction of major graph elements and tools that we will use to control them. So, let's build some major physics equations. Go on and construct an Einstein formula E = mc^2. Notice, that here we see an additional element, a constant 2. It does not require any special knowledge about it, treat it in the same fashion as a variable. As in the previous exercise the left side of the equation is prebuilt. You do not have to modify it.	{"edges": {}, "nodes": {"8": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "E", "xpos": 2, "ypos": 2}, "9": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "m", "xpos": 4, "ypos": 2}, "10": {"state": "unknown", "type": "V", "unit": "", "value": "", "varName": "c", "xpos": 4, "ypos": 3}, "11": {"type": "C", "unit": "", "value": "2", "varName": "2", "xpos": 4, "ypos": 4}, "12": {"type": "MG", "xpos": 3, "ypos": 3}, "13": {"parsed": "-E+m*c**2", "parsing": "-E+c**2.0*m", "type": "E", "xpos": 3, "ypos": 2}, "14": {"type": "PG", "xpos": 3, "ypos": 4}}}	15	\N	1	1
16	1	Second famous formula to be built is a Pythagoras formel c^2 = a^2 + b^2. As in the previous exercise the left side of the equation is prebuilt.	{"edges": {}, "nodes": {"11": {"type": "V", "xpos": 2, "ypos": 3, "varName": "a", "unit": "", "value": "", "state": "unknown"}, "12": {"type": "V", "xpos": 2, "ypos": 5, "varName": "b", "unit": "", "value": "", "state": "unknown"}, "13": {"type": "V", "xpos": 2, "ypos": 7, "varName": "c", "unit": "", "value": "", "state": "unknown"}, "14": {"type": "C", "xpos": 2, "ypos": 4, "varName": "2", "unit": "", "value": "2"}, "15": {"type": "C", "xpos": 2, "ypos": 2, "varName": "2", "unit": "", "value": "2"}, "16": {"type": "C", "xpos": 2, "ypos": 6, "varName": "2", "unit": "", "value": "2"}, "17": {"type": "E", "xpos": 6, "ypos": 7, "parsed": true, "parsing": "a**2.0+b**2.0-c**2.0"}, "18": {"type": "PG", "xpos": 4, "ypos": 3}, "19": {"type": "PG", "xpos": 4, "ypos": 7}, "20": {"type": "PG", "xpos": 4, "ypos": 5}}}	16	\N	1	1
17	1	Now let's switch up a gear and go for multiple equations, or in other words, equation systems. First, let's construct the simplest equation system: Equation 1 on the top (a = 1 + b) and Equation 2 on the bottom (a = b). Left parts of both equations were present for simplicity. \n\nTip: do both equations independently, as they would be the only one. Do not be confused that variables are connected with multiple equations.	{"edges": {"3": {"origin": 6, "target": 9, "weight": -1}, "4": {"origin": 6, "target": 8, "weight": -1}}, "nodes": {"6": {"type": "V", "xpos": 2, "ypos": 8, "varName": "a", "unit": "", "value": "", "state": "unknown"}, "7": {"type": "V", "xpos": 4, "ypos": 8, "varName": "b", "unit": "", "value": "", "state": "unknown"}, "8": {"type": "E", "xpos": 3, "ypos": 9, "parsed": true, "parsing": "-a+b"}, "9": {"type": "E", "xpos": 3, "ypos": 7, "parsed": true, "parsing": "-a+b+1.0"}, "10": {"type": "C", "xpos": 3, "ypos": 6, "varName": "1", "unit": "", "value": 1}}}	17	\N	1	1
18	1	To spice things up try to complete the system of three equations. Equation 1 (a = b * c) is on the top left, Equation 2 (b = a^c) is on the right and Equation 3 (c = a + b) is on the bottom. Left sides as always are present.	{"edges": {"4": {"origin": 10, "target": 14, "weight": -1}, "5": {"origin": 12, "target": 15, "weight": -1}, "6": {"origin": 11, "target": 13, "weight": -1}}, "nodes": {"10": {"type": "V", "xpos": 3, "ypos": 2, "varName": "a", "unit": "", "value": "", "state": "unknown"}, "11": {"type": "V", "xpos": 4, "ypos": 6, "varName": "b", "unit": "", "value": "", "state": "unknown"}, "12": {"type": "V", "xpos": 7, "ypos": 3, "varName": "c", "unit": "", "value": "", "state": "unknown"}, "13": {"type": "E", "xpos": 4, "ypos": 8, "parsed": "a-b+c", "parsing": "a**c-b"}, "14": {"type": "E", "xpos": 1, "ypos": 3, "parsed": true, "parsing": "-a+b*c"}, "15": {"type": "E", "xpos": 9, "ypos": 4, "parsed": "a**c-b", "parsing": "a+b-c"}, "16": {"type": "MG", "xpos": 3, "ypos": 3}, "17": {"type": "SG", "xpos": 7, "ypos": 4}, "18": {"type": "PG", "xpos": 5, "ypos": 6}}}	18	\N	1	1
19	1	Now we will solve our first problem on the graph with the second Newton's law. Given that the car of mass 2000 kg is accelerating with 10m/s^2. We will find the torque generated by the motor. \n\nThe difference here is that now the variable mass and acceleration are known (yellow). The variable force is a solution variable (violet). \n\nGo on, finish the 2nd Newton Law (F = ma) and press CHECK to solve this exercise and calculate the force from this graph.	{"edges": {"2": {"origin": 6, "target": 9, "weight": -1}}, "nodes": {"6": {"state": "solution", "type": "V", "unit": "newton", "value": "20000", "varName": "F", "xpos": 2, "ypos": 5}, "7": {"state": "known", "type": "V", "unit": "kg", "value": "2000", "varName": "m", "xpos": 8, "ypos": 4}, "8": {"state": "known", "type": "V", "unit": "m/s**2", "value": "10", "varName": "a", "xpos": 8, "ypos": 6}, "9": {"type": "E", "xpos": 4, "ypos": 5}, "10": {"type": "MG", "xpos": 6, "ypos": 5}}}	19	\N	1	1
20	1	Now we are going to solve our first real problem as a final challenge. \n\nProblem: Car of mass m1 = 2000 kg with passengers of a total mass m2 = 250 kg is accelerating on the highway with force of F1 = 20000 N produced by the engine. Calculate the acceleration, if the car is experiencing total resistance of 1000 N from the wind and road. \n\nFirst of all, construct the equation that will calculate  total mass M from m1 and m2.	{"edges": {"2": {"origin": 7, "target": 8, "weight": -1}}, "nodes": {"5": {"type": "V", "xpos": 8, "ypos": 1, "varName": "m1", "unit": "kg", "value": "2000", "state": "known"}, "6": {"type": "V", "xpos": 8, "ypos": 5, "varName": "m2", "unit": "kg", "value": "250", "state": "known"}, "7": {"type": "V", "xpos": 6, "ypos": 3, "varName": "m", "unit": "kg", "value": "", "state": "unknown"}, "8": {"type": "E", "xpos": 8, "ypos": 3, "parsed": "-m+m1+m2", "parsing": "2250.0-m"}}}	20	\N	1	1
21	1	Problem: Car of mass m0 = 2000 kg with passengers of a total mass m1 = 250 kg is accelerating on the highway with force of F1 = 20000 N produced by the engine. Calculate the acceleration, if the car is experiencing total resistance of 1000 N from the wind and road. \n\nNow, construct the second equation that will calculate the total force F from engine force F1 and resistance force F2.	{"edges": {"5": {"origin": 11, "target": 16, "weight": -1}, "6": {"origin": 14, "target": 15, "weight": -1}, "7": {"origin": 9, "target": 16, "weight": 1}, "8": {"origin": 10, "target": 16, "weight": 1}}, "nodes": {"9": {"type": "V", "xpos": 8, "ypos": 2, "varName": "m1", "unit": "kg", "value": "2000", "state": "known"}, "10": {"type": "V", "xpos": 8, "ypos": 6, "varName": "m2", "unit": "kg", "value": "250", "state": "known"}, "11": {"type": "V", "xpos": 6, "ypos": 4, "varName": "M", "unit": "kg", "value": "", "state": "unknown"}, "12": {"type": "V", "xpos": 2, "ypos": 2, "varName": "F1", "unit": "N", "value": "20000", "state": "known"}, "13": {"type": "V", "xpos": 2, "ypos": 6, "varName": "F2", "unit": "N", "value": "1000", "state": "known"}, "14": {"type": "V", "xpos": 4, "ypos": 4, "varName": "F", "unit": "N", "value": "", "state": "unknown"}, "15": {"type": "E", "xpos": 2, "ypos": 4, "parsed": "19000-F", "parsing": "19000.0-F"}, "16": {"type": "E", "xpos": 8, "ypos": 4, "parsed": false}}}	21	\N	1	1
22	1	Problem: Car of mass m0 = 2000 kg with passengers of a total mass m1 = 250 kg is accelerating on the highway with force of F1 = 20000 N produced by the engine. Calculate the acceleration, if the car is experiencing total resistance of 1000 N from the wind and road. \n\nFinally, construct the last equation that will calculate the acceleration from force F and mass M.	{"edges": {"7": {"origin": 16, "target": 19, "weight": -1}, "8": {"origin": 17, "target": 19, "weight": -1}, "9": {"origin": 14, "target": 21, "weight": -1}, "10": {"origin": 15, "target": 19, "weight": 1}, "11": {"origin": 12, "target": 21, "weight": 1}, "12": {"origin": 13, "target": 21, "weight": 1}, "13": {"origin": 17, "target": 20, "weight": -1}}, "nodes": {"12": {"state": "known", "type": "V", "unit": "kg", "value": "2000", "varName": "m1", "xpos": 8, "ypos": 2}, "13": {"state": "known", "type": "V", "unit": "kg", "value": "250", "varName": "m2", "xpos": 8, "ypos": 6}, "14": {"state": "unknown", "type": "V", "unit": "kg", "value": "", "varName": "M", "xpos": 6, "ypos": 4}, "15": {"state": "known", "type": "V", "unit": "N", "value": "20000", "varName": "F1", "xpos": 2, "ypos": 2}, "16": {"state": "known", "type": "V", "unit": "N", "value": "1000", "varName": "F2", "xpos": 2, "ypos": 6}, "17": {"state": "unknown", "type": "V", "unit": "N", "value": "", "varName": "F", "xpos": 4, "ypos": 4}, "18": {"state": "solution", "type": "V", "unit": "m/s**2", "value": "8.444444444444445", "varName": "a", "xpos": 6, "ypos": 8}, "19": {"type": "E", "xpos": 2, "ypos": 4}, "20": {"type": "E", "xpos": 4, "ypos": 6}, "21": {"type": "E", "xpos": 8, "ypos": 4}, "22": {"type": "MG", "xpos": 6, "ypos": 6}}}	22	\N	1	1
23	1	Now we will try to solve previous exercises with the help of skills. Once, we create a skill that stays with us and we can use it in later exercises.\n\nSo, let us learn our first skill. It will be the most famous equation of motion, the second Newton's law.\n\nIn order to build our first skill go on and construct the equation F = m * a from its building blocks.	{"edges": {}, "nodes": {"6": {"state": "unknown", "type": "V", "unit": "N", "value": "", "varName": "F", "xpos": 1, "ypos": 4}, "7": {"state": "unknown", "type": "V", "unit": "kg", "value": "", "varName": "m", "xpos": 2, "ypos": 4}, "8": {"state": "unknown", "type": "V", "unit": "m/s**2", "value": "", "varName": "a", "xpos": 3, "ypos": 4}, "9": {"parsed": "-F+m*a", "parsing": "-F+a*m", "type": "E", "xpos": 1, "ypos": 5}, "10": {"type": "MG", "xpos": 2, "ypos": 5}}}	23	\N	1	1
24	1	For the solution of the problem we will need one more skill. It will be the universal superposition principle.\n\nIn order to build this skill go on and construct the equation x = x1 + x2 from its building blocks.	{"edges": {}, "nodes": {"5": {"type": "E", "xpos": 1, "ypos": 3, "parsed": true, "parsing": "-x+x1+x2"}, "6": {"type": "V", "xpos": 1, "ypos": 2, "varName": "x", "unit": "", "value": "", "state": "unknown"}, "7": {"type": "V", "xpos": 2, "ypos": 2, "varName": "x1", "unit": "", "value": "", "state": "unknown"}, "8": {"type": "V", "xpos": 3, "ypos": 2, "varName": "x2", "unit": "", "value": "", "state": "unknown"}}}	24	\N	1	1
25	1	Now, as promised, let us solve our problem with help of our freshly learned skills.\n\nProblem: Car of mass m1 = 2000 kg with passengers of a total mass m2 = 250 kg is accelerating on the highway with force of F1 = 20000 N produced by the engine. Calculate the acceleration, if the car is experiencing total resistance of 1000 N from the wind and road. \n\nFirst, let us calculate the total mass of the car with help of the superposition principle. Click on the skill tool (backpack icon) and select the superposition principle. The graph of the skill will appear. You can move this graph by holding Shift and arrow keys.\n\nNow insert known variables (m1 and m2) and solution variable (m) in the skill graph with help of the fusion tool (the last one). For this click on the fusion tool and drag the known variable to the place, where you want to insert it in the skill graph. In this case (m->x), (m1->x1) and (m2->x2).	{"edges": {}, "nodes": {"4": {"type": "V", "xpos": 1, "ypos": 2, "varName": "m1", "unit": "kg", "value": "2000", "state": "known"}, "5": {"type": "V", "xpos": 2, "ypos": 2, "varName": "m2", "unit": "kg", "value": "250", "state": "known"}, "6": {"type": "V", "xpos": 3, "ypos": 2, "varName": "m", "unit": "kg", "value": "", "state": "unknown"}}}	25	\N	1	1
26	1	Problem: Car of mass m1 = 2000 kg with passengers of a total mass m2 = 250 kg is accelerating on the highway with force of F1 = 20000 N produced by the engine. Calculate the acceleration, if the car is experiencing total resistance of 1000 N from the wind and road. \n\nNow let us calculate the total force acting upon the car with help of the superposition principle graph in a similar fashion as we did with mass calculation. \n\nFor this go to the skill tool (backpack) again, select superposition principle and insert F, F1 and F2 into the skill graph with help of fusion tool.\n\nIf needed, do not hesitate and change the edge connecting F2 to the F to a negative one.	{"nodes": {"1": {"xpos": 9, "SolutionVar": false, "varName": "m2", "ypos": 3, "value": 250.0, "known": true, "type": "V", "unit": "kg"}, "3": {"xpos": 7, "SolutionVar": false, "known": false, "varName": "m", "type": "V", "ypos": 2, "unit": "kg"}, "2": {"xpos": 9, "SolutionVar": false, "varName": "m1", "ypos": 1, "value": 2000.0, "known": true, "type": "V", "unit": "kg"}, "5": {"xpos": 2, "SolutionVar": true, "varName": "F", "ypos": 1, "ExpectedValue": "19000", "known": false, "type": "V", "unit": "N"}, "4": {"xpos": 8, "type": "E", "ypos": 2}, "7": {"xpos": 4, "unit": "N", "known": true, "varName": "F2", "type": "V", "ypos": 1, "value": 1000.0}, "6": {"xpos": 3, "unit": "N", "known": true, "varName": "F1", "type": "V", "ypos": 1, "value": 20000.0}}, "edges": {"1": {"origin": 1, "target": 4, "weight": 1.0}, "3": {"origin": 2, "target": 4, "weight": 1.0}, "2": {"origin": 3, "target": 4, "weight": -1.0}}}	26	\N	1	1
28	2	Hello! My name is Mario and I am an astronaut. I am planning to be the first man on Mars. There is only one problem, I do not understand Physics and during my venture I will often ask for your help. \n\nBefore we begin, I would like you to learn your first skill of homogeneous motion.\n\nIn order to learn this skill go on and construct the equation L = v * T from its building blocks, length (L), velocity (v) and time (T).	{"nodes": {"1": {"xpos": 1, "type": "E", "ypos": 2, "ExpectedParsing": "-1.0*L+1.0*T*v"}, "3": {"xpos": 1, "SolutionVar": false, "known": false, "varName": "L", "type": "V", "ypos": 1, "unit": "km"}, "2": {"xpos": 2, "SolutionVar": false, "known": false, "varName": "v", "type": "V", "ypos": 1, "unit": "km/hour"}, "5": {"xpos": 2, "type": "MG", "ypos": 2}, "4": {"xpos": 3, "SolutionVar": false, "known": false, "varName": "T", "type": "V", "ypos": 1, "unit": "hour"}}, "edges": {}}	1	\N	1	1
29	2	Today is the first day of my training. I am driving to the space agency on the highway. I have to be there exactly in (T = 2 hours). What speed (v) should I keep, if the way to the space agency is exactly (L = 240 km)?\n\nUse your homogeneous motion skill with given variables to find out the speed for Mario.	{"nodes": {"1": {"xpos": 2, "SolutionVar": true, "varName": "v", "ypos": 1, "ExpectedValue": "120.0", "known": false, "type": "V", "unit": "km/hour"}, "3": {"xpos": 3, "SolutionVar": false, "varName": "T", "ypos": 1, "value": 2.0, "known": true, "type": "V", "unit": "hour"}, "2": {"xpos": 1, "SolutionVar": false, "varName": "L", "ypos": 1, "value": 240.0, "known": true, "type": "V", "unit": "km"}}, "edges": {}}	2	\N	1	1
30	2	After a short introduction from NASA officials Mario goes straight to his first exercise, which is an endurance swimming. Mario covered (L1=1km) breaststroke and a (L2=4km) cowl part.\n\nFigure out his average swimming pace (v-?) is the training took (T = 1 hour)  so that he knows what to put in NASA exercise spreadsheet.\n\nUse the homogeneous motion skill to find out Mario's average swimming pace. Use a superposition skill to figure out the swim length L out of L1 and L2.	{"nodes": {"1": {"xpos": 1, "SolutionVar": false, "varName": "L1", "ypos": 1, "value": 1.0, "known": true, "type": "V", "unit": "km"}, "3": {"xpos": 2, "unit": "km", "known": true, "varName": "L2", "type": "V", "ypos": 1, "value": 4.0}, "2": {"xpos": 3, "SolutionVar": false, "varName": "T", "ypos": 1, "value": 1.0, "known": true, "type": "V", "unit": "hour"}, "4": {"xpos": 4, "SolutionVar": true, "varName": "v", "ypos": 1, "ExpectedValue": "5.0", "known": false, "type": "V", "unit": "kilometer/hour"}}, "edges": {}}	3	\N	1	1
31	2	Now the time comes for a swimming test. Mario competes against his personal trainer. \n\nDuring the time that Mario needs to swim his usual (L1 = 5km), his trainer covers stunning (L2 = 7km). Calculate Mario's average speed v1, if his trainer averages (v2 = 7 km/h).\n\nUse the homogeneous motion skill twice, for description of  Mario's and trainer's swim (remember that the time T is the same for both).	{"nodes": {"1": {"xpos": 4, "SolutionVar": false, "varName": "L1", "ypos": 1, "value": 5.0, "known": true, "type": "V", "unit": "kilometer"}, "3": {"xpos": 2, "SolutionVar": false, "varName": "v2", "ypos": 1, "value": 7.0, "known": true, "type": "V", "unit": "m/s"}, "2": {"xpos": 3, "SolutionVar": false, "varName": "L2", "ypos": 1, "value": 7.0, "known": true, "type": "V", "unit": "kilometer"}, "4": {"xpos": 5, "SolutionVar": true, "varName": "v1", "ypos": 1, "ExpectedValue": "5.0", "known": false, "type": "V", "unit": "kilometer / hour"}}, "edges": {}}	4	\N	2	1
32	2	Today, it is time to test Mario swimming skills in a river. He has to cover the training distance (L = 8 km) downstream the river. Calculate Mario’s swimming pace relative to water (v1), if he covered the distance in (T=1 hour) and the river speed is (v0 = 3 km/h).	{"nodes": {"1": {"xpos": 3, "SolutionVar": false, "varName": "T", "ypos": 1, "value": 1.0, "known": true, "type": "V", "unit": "hour"}, "0": {"xpos": 4, "SolutionVar": false, "varName": "L", "ypos": 1, "value": 8.0, "known": true, "type": "V", "unit": "kilometer"}, "2": {"xpos": 2, "SolutionVar": false, "varName": "v0", "ypos": 1, "value": 3.0, "known": true, "type": "V", "unit": "kilometer / hour"}, "4": {"xpos": 5, "ExpectedValue": "5.0", "SolutionVar": true, "varName": "v1", "type": "V", "ypos": 1, "unit": "kilometer / hour"}}, "edges": {}}	5	\N	2	1
33	2	Now it is time to learn a new skill, accelerated motion (velocity definition).\n\nIn order to learn this skill go on and construct the equation v1 = v0 + a * T from its building blocks.	{"nodes": {"1": {"xpos": 1, "type": "E", "ypos": 2, "ExpectedParsing": "1.0*T*a+1.0*v0-1.0*v1"}, "3": {"xpos": 2, "SolutionVar": false, "known": false, "varName": "v0", "type": "V", "ypos": 1, "unit": "meter / second"}, "2": {"xpos": 1, "SolutionVar": false, "known": false, "varName": "v1", "type": "V", "ypos": 1, "unit": "meter / second"}, "5": {"xpos": 2, "type": "MG", "ypos": 2}, "4": {"xpos": 4, "SolutionVar": false, "known": false, "varName": "T", "type": "V", "ypos": 1, "unit": "hour"}, "6": {"xpos": 3, "varName": "a", "ypos": 1, "type": "V", "unit": "meter / s / s"}}, "edges": {}}	6	\N	2	1
34	2	Swimming was never Mario's favourite after all. But athletics is a totally different story. Back at school he was top of his class. Today he goes to the NASA athletics field for the first time.\n\nOnce, when he was running at speed of (v0=12km/h) he was called by his mentor. He stopped abruptly (v1=0km/h) in (T=0.5s) to answer. Figure out the acceleration Mario experienced (a-?) during stopping.\n\nUse freshly learned accelerated motion skill to find out Mario's acceleration.	{"nodes": {"1": {"xpos": 1, "SolutionVar": false, "varName": "v1", "ypos": 1, "value": 0.0, "known": true, "type": "V", "unit": "kilometer / hour"}, "3": {"xpos": 2, "SolutionVar": false, "varName": "v0", "ypos": 1, "value": 12.0, "known": true, "type": "V", "unit": "kilometer / hour"}, "2": {"xpos": 3, "SolutionVar": false, "varName": "T", "ypos": 1, "value": 0.5, "known": true, "type": "V", "unit": "second"}, "4": {"xpos": 4, "SolutionVar": true, "varName": "a", "ypos": 1, "ExpectedValue": "-24.0", "known": false, "type": "V", "unit": "kilometer / hour / second"}}, "edges": {}}	7	\N	2	1
35	2	During the relay race Mario has to receive a baton from his team mate. The idea is that after the transfer of a baton Mario has to accelerate to a final speed (v1), which is equal to the final speed of his teammate. Unfortunately, Mario does not know this speed, he only knows that his teammate will run last (L*=10m) in (T*=2s).\n\nFigure out how long (T-?) Mario will have to run with acceleration of (a=5m/s^2) to reach his final speed? For this exercise we will assume that the initial speed of Mario was (v0=0m/s).	{"nodes": {"1": {"xpos": 1, "SolutionVar": false, "varName": "L*", "ypos": 1, "value": 10.0, "known": true, "type": "V", "unit": "meter"}, "3": {"xpos": 3, "SolutionVar": false, "varName": "v0", "ypos": 1, "value": 0.0, "known": true, "type": "V", "unit": "meter / second"}, "2": {"xpos": 2, "SolutionVar": false, "varName": "T*", "ypos": 1, "value": 2.0, "known": true, "type": "V", "unit": "second"}, "5": {"xpos": 5, "SolutionVar": true, "varName": "T", "ypos": 1, "ExpectedValue": "1.0", "known": false, "type": "V", "unit": "second"}, "4": {"xpos": 4, "SolutionVar": false, "varName": "a", "ypos": 1, "value": 5.0, "known": true, "type": "V", "unit": "meter / second / second"}}, "edges": {}}	8	\N	2	1
36	2	After consulting with his trainer Mario understands that he has to start running even before he receives the baton. This time, after receiving the baton he accelerates with (a=5m/s^2) for (T=0.5s) to a final speed, which is twice higher than his initial speed. Figure out Mario’s final speed (v1-?).\n\nThis time you will have to modify the accelerated motion skill graph to add the condition v1 = v0 * 2.	{"nodes": {"1": {"xpos": 1, "SolutionVar": false, "varName": "a", "ypos": 1, "value": 5.0, "known": true, "type": "V", "unit": "meter / second / second"}, "0": {"xpos": 4, "SolutionVar": true, "varName": "v1", "ypos": 1, "ExpectedValue": "5.0", "known": false, "type": "V", "unit": "meter / second"}, "2": {"xpos": 2, "SolutionVar": false, "varName": "T", "ypos": 1, "value": 0.5, "known": true, "type": "V", "unit": "second"}, "5": {"xpos": 1, "type": "E", "ypos": 2}, "4": {"xpos": 3, "unit": "dimensionless", "varName": "2", "type": "C", "ypos": 1, "value": 2.0}, "6": {"xpos": 2, "type": "MG", "ypos": 2}}, "edges": {}}	9	\N	2	1
37	2	As a test of the maximum achievable running speed trainer makes students run on a treadmill that constantly accelerates from zero speed (v0=0m/s) and measures time, that student is able to endure it. Mario’s friend is a professional runner. He was able to stand on it for (T* = 3min) and he achieved stunning (v* = 21km/h). Unfortunately, Mario only lasted for (T = 2min). Figure out Mario’s maximum speed (v1-?).	{"nodes": {"1": {"xpos": 5, "SolutionVar": true, "varName": "v1", "ypos": 1, "ExpectedValue": "14", "known": false, "type": "V", "unit": "kilometer / hour"}, "3": {"xpos": 4, "SolutionVar": false, "varName": "T", "ypos": 1, "value": 2.0, "known": true, "type": "V", "unit": "minute"}, "2": {"xpos": 2, "SolutionVar": false, "varName": "T*", "ypos": 1, "value": 3.0, "known": true, "type": "V", "unit": "minute"}, "5": {"xpos": 1, "unit": "kilometer / hour", "known": true, "varName": "v0", "type": "V", "ypos": 1, "value": 0.0}, "4": {"xpos": 3, "unit": "kilometer / hour", "known": true, "varName": "v*", "type": "V", "ypos": 1, "value": 21.0}}, "edges": {}}	10	\N	2	1
38	2	Now it is time to learn a new skill, accelerated motion (coordinate definition).\n\nIn order to learn this skill go on and construct the equation x1 = x0 + v0 * T + 0.5 * a * T^2 from its building blocks. For the term (0.5aT^2) remember that all 3 elements can be connected to the same multiplication gate.	{"nodes": {"11": {"xpos": 7, "unit": "dimensionless", "varName": "2", "type": "C", "ypos": 1, "value": 2.0}, "10": {"xpos": 4, "type": "PG", "ypos": 2}, "1": {"xpos": 1, "type": "E", "ypos": 2, "ExpectedParsing": "1.0*T*v0+0.5*T**2.0*a+1.0*x0-1.0*x1"}, "3": {"xpos": 3, "SolutionVar": false, "known": false, "varName": "v0", "type": "V", "ypos": 1, "unit": "meter / second"}, "2": {"xpos": 1, "SolutionVar": false, "known": false, "varName": "x1", "type": "V", "ypos": 1, "unit": "meter"}, "5": {"xpos": 2, "type": "MG", "ypos": 2}, "4": {"xpos": 4, "SolutionVar": false, "known": false, "varName": "T", "type": "V", "ypos": 1, "unit": "hour"}, "7": {"xpos": 2, "varName": "x0", "ypos": 1, "type": "V", "unit": "meter"}, "6": {"xpos": 5, "varName": "a", "ypos": 1, "type": "V", "unit": "meter / s / s"}, "9": {"xpos": 3, "type": "MG", "ypos": 2}, "8": {"xpos": 6, "unit": "dimensionless", "varName": "1/2", "type": "C", "ypos": 1, "value": 0.5}}, "edges": {}}	11	\N	2	1
39	2	In order to simplify the use of the accelerated motion skill we will learn 2 simplified versions of this skill.\n \nFirst, let us rewrite the formula in terms of displacement. Construct the equation L = v0 * T + 0.5 * a * T^2 by simplifying the general form of accelerated motion that we previously learned.\n\nIn order to finish this exercise you will need to remove some variable nodes representing coordinates. Use a node removal tool for that (crossed square node).	{"nodes": {"11": {"xpos": 4, "type": "PG", "ypos": 4, "power": 12}, "10": {"xpos": 3, "type": "MG", "ypos": 4}, "12": {"xpos": 4, "unit": "dimensionless", "varName": "2", "type": "C", "ypos": 5, "value": 2.0}, "1": {"xpos": 1, "SolutionVar": false, "known": false, "varName": "L", "type": "V", "ypos": 1, "unit": "meter"}, "3": {"xpos": 2, "SolutionVar": false, "known": false, "varName": "x1", "type": "V", "ypos": 3, "unit": "meter"}, "2": {"xpos": 3, "type": "E", "ypos": 3, "ExpectedParsing": "-1.0*L+1.0*T*v0+0.5*T**2.0*a"}, "5": {"xpos": 5, "SolutionVar": false, "known": false, "varName": "T", "type": "V", "ypos": 3, "unit": "hour"}, "4": {"xpos": 4, "SolutionVar": false, "known": false, "varName": "v0", "type": "V", "ypos": 2, "unit": "meter / second"}, "7": {"xpos": 3, "varName": "a", "ypos": 5, "type": "V", "unit": "meter / s / s"}, "6": {"xpos": 4, "type": "MG", "ypos": 3}, "9": {"xpos": 2, "unit": "dimensionless", "varName": "1/2", "type": "C", "ypos": 4, "value": 0.5}, "8": {"xpos": 3, "varName": "x0", "ypos": 2, "type": "V", "unit": "meter"}}, "edges": {"11": {"origin": 4, "target": 6, "weight": 1.0}, "10": {"origin": 5, "target": 6, "weight": 1.0}, "1": {"origin": 12, "PI": true, "target": 11, "weight": 1.0}, "3": {"origin": 11, "target": 10, "weight": 1.0}, "2": {"origin": 5, "target": 11, "weight": 1.0}, "5": {"origin": 7, "target": 10, "weight": 1.0}, "4": {"origin": 9, "target": 10, "weight": 1.0}, "7": {"origin": 3, "target": 2, "weight": -1.0}, "6": {"origin": 10, "target": 2, "weight": 1.0}, "9": {"origin": 6, "target": 2, "weight": 1.0}, "8": {"origin": 8, "target": 2, "weight": 1.0}}}	12	\N	2	1
40	2	In order to simplify the use of the accelerated motion skill we will learn 2 simplified versions of this skill.\n \nSecond, let us assume that the initial speed is zero. Construct the equation L = 0.5 * a * T^2 by simplifying the general form of accelerated motion that we previously learned.\n\nDo not forget to remove the multiplication gate, that connects v0 variable to the equation.	{"nodes": {"10": {"xpos": 4, "unit": "dimensionless", "varName": "2", "type": "C", "ypos": 5, "value": 2.0}, "1": {"xpos": 2, "SolutionVar": false, "known": false, "varName": "L", "type": "V", "ypos": 3, "unit": "meter"}, "3": {"xpos": 4, "SolutionVar": false, "known": false, "varName": "v0", "type": "V", "ypos": 2, "unit": "meter / second"}, "2": {"xpos": 3, "type": "E", "ypos": 3, "ExpectedParsing": "-1.0*L+0.5*T**2.0*a"}, "5": {"xpos": 4, "type": "MG", "ypos": 3}, "4": {"xpos": 5, "SolutionVar": false, "known": false, "varName": "T", "type": "V", "ypos": 3, "unit": "hour"}, "7": {"xpos": 2, "unit": "dimensionless", "varName": "1/2", "type": "C", "ypos": 4, "value": 0.5}, "6": {"xpos": 3, "varName": "a", "ypos": 5, "type": "V", "unit": "meter / s / s"}, "9": {"xpos": 4, "type": "PG", "ypos": 4, "power": 10}, "8": {"xpos": 3, "type": "MG", "ypos": 4}}, "edges": {"10": {"origin": 6, "target": 8, "weight": 1.0}, "1": {"origin": 1, "target": 2, "weight": -1.0}, "3": {"origin": 5, "target": 2, "weight": 1.0}, "2": {"origin": 8, "target": 2, "weight": 1.0}, "5": {"origin": 4, "target": 5, "weight": 1.0}, "4": {"origin": 3, "target": 5, "weight": 1.0}, "7": {"origin": 4, "target": 9, "weight": 1.0}, "6": {"origin": 10, "PI": true, "target": 9, "weight": 1.0}, "9": {"origin": 7, "target": 8, "weight": 1.0}, "8": {"origin": 9, "target": 8, "weight": 1.0}}}	13	\N	2	1
41	2	Let us come back to the relay race. After the transfer of a baton Mario accelerates with (a=5m/s^2) for (T = 1s). Figure out the distance that Mario covers during the acceleration, if he starts from a resting position (v0 = 0m/s).	{"nodes": {"1": {"xpos": 4, "SolutionVar": true, "varName": "L", "ypos": 1, "ExpectedValue": "2.5", "known": false, "type": "V", "unit": "meter"}, "3": {"xpos": 2, "SolutionVar": false, "varName": "T", "ypos": 1, "value": 1.0, "known": true, "type": "V", "unit": "second"}, "2": {"xpos": 3, "SolutionVar": false, "varName": "v0", "ypos": 1, "value": 0.0, "known": true, "type": "V", "unit": "meter / second"}, "4": {"xpos": 1, "SolutionVar": false, "varName": "a", "ypos": 1, "value": 5.0, "known": true, "type": "V", "unit": "meter / s / s"}}, "edges": {}}	14	\N	2	1
44	1	Demo text	{"edges": {}, "nodes": {}}	27	\N	2	1
45	2	Demo text22	{"edges": {"1": {"origin": 2, "target": 3, "weight": 1}, "2": {"origin": 1, "target": 3, "weight": -1}}, "nodes": {"1": {"type": "V", "xpos": 3, "ypos": 3, "varName": "a", "unit": "", "value": "", "state": "unknown"}, "2": {"varName": "b", "type": "V", "unit": "", "state": "unknown", "value": "", "xpos": 5, "ypos": 5}, "3": {"type": "E", "xpos": 6, "ypos": 3}}}	16	\N	1	1
\.


--
-- Data for Name: skills; Type: TABLE DATA; Schema: public; Owner: physai_admin
--

COPY public.skills (id, name, graph, front_graph, equation) FROM stdin;
1	Second Newton Law	{"nodes": {"6": {"varName": "m", "type": "V", "unit": "", "state": "unknown", "value": "", "xpos": 8, "ypos": 1}, "7": {"varName": "F", "type": "V", "unit": "", "state": "unknown", "value": "", "xpos": 2, "ypos": 2}, "8": {"type": "V", "xpos": 8, "ypos": 3, "varName": "a", "unit": "", "value": "", "state": "unknown"}, "9": {"type": "MG", "xpos": 6, "ypos": 2}, "10": {"type": "E", "xpos": 4, "ypos": 2}}, "edges": {"5": {"origin": 7, "target": 10, "weight": -1}, "6": {"origin": 9, "target": 10, "weight": 1}, "7": {"origin": 6, "target": 9, "weight": 1}, "8": {"origin": 8, "target": 9, "weight": 1}}}	{"nodes": {"0": {"type": "SKILL", "skillID": 1, "skillName": "Second Newton Law", "skillEQ": "$$ F = ma $$", "xpos": 2, "ypos": 2}, "6": {"varName": "m", "type": "V", "unit": "", "state": "unknown", "value": "", "xpos": 1, "ypos": 1, "skillVarLink": 6}, "7": {"varName": "F", "type": "V", "unit": "", "state": "unknown", "value": "", "xpos": 2, "ypos": 1, "skillVarLink": 7}, "8": {"type": "V", "xpos": 3, "ypos": 1, "varName": "a", "unit": "", "value": "", "state": "unknown", "skillVarLink": 8}}, "edges": {"1": {"origin": 6, "target": 0, "weight": 1}, "2": {"origin": 7, "target": 0, "weight": 1}, "3": {"origin": 8, "target": 0, "weight": 1}}}	$$ F = ma $$
2	Superposition Principle	{"nodes": {"1": {"xpos": 2, "type": "E", "ypos": 2}, "3": {"xpos": 3, "SolutionVar": false, "known": false, "varName": "x2", "type": "V", "ypos": 3, "unit": "dimensionless"}, "2": {"xpos": 1, "SolutionVar": false, "known": false, "varName": "x", "type": "V", "ypos": 2, "unit": "dimensionless"}, "4": {"xpos": 3, "SolutionVar": false, "known": false, "varName": "x1", "type": "V", "ypos": 1, "unit": "dimensionless"}}, "edges": {"1": {"origin": 3, "target": 1, "weight": 1.0}, "3": {"origin": 4, "target": 1, "weight": 1.0}, "2": {"origin": 2, "target": 1, "weight": -1.0}}}	{"nodes": {"0": {"xpos": 2, "skillName": "Superposition Principle", "ypos": 2, "type": "SKILL", "skillEQ": "x = x1 + x2", "skillID": 2}, "3": {"xpos": 1, "SolutionVar": false, "varName": "x2", "ypos": 1, "skillVarLink": 3, "known": false, "type": "V", "unit": "dimensionless"}, "2": {"xpos": 2, "SolutionVar": false, "varName": "x", "ypos": 1, "skillVarLink": 2, "known": false, "type": "V", "unit": "dimensionless"}, "4": {"xpos": 3, "SolutionVar": false, "varName": "x1", "ypos": 1, "skillVarLink": 4, "known": false, "type": "V", "unit": "dimensionless"}}, "edges": {"1": {"origin": 3, "target": 0, "weight": 2}, "3": {"origin": 4, "target": 0, "weight": 2}, "2": {"origin": 2, "target": 0, "weight": 2}}}	$$ x = x_1 + x_2 $$
3	Homogeneous Motion	{"nodes": {"1": {"xpos": 1, "SolutionVar": false, "known": false, "varName": "L", "type": "V", "ypos": 2, "unit": "meter"}, "3": {"xpos": 4, "SolutionVar": false, "known": false, "varName": "v", "type": "V", "ypos": 1, "unit": "m/s"}, "2": {"xpos": 4, "SolutionVar": false, "known": false, "varName": "T", "type": "V", "ypos": 3, "unit": "second"}, "5": {"xpos": 2, "type": "E", "ypos": 2}, "4": {"xpos": 3, "type": "MG", "ypos": 2}}, "edges": {"1": {"origin": 1, "target": 5, "weight": -1.0}, "3": {"origin": 3, "target": 4, "weight": 1.0}, "2": {"origin": 4, "target": 5, "weight": 1.0}, "4": {"origin": 2, "target": 4, "weight": 1.0}}}	{"nodes": {"1": {"xpos": 1, "SolutionVar": false, "varName": "L", "ypos": 1, "skillVarLink": 1, "known": false, "type": "V", "unit": "meter"}, "0": {"xpos": 2, "skillName": "Homogeneous Motion", "ypos": 2, "type": "SKILL", "skillEQ": "L = v * T", "skillID": 3}, "3": {"xpos": 2, "SolutionVar": false, "varName": "v", "ypos": 1, "skillVarLink": 3, "known": false, "type": "V", "unit": "m/s"}, "2": {"xpos": 3, "SolutionVar": false, "varName": "T", "ypos": 1, "skillVarLink": 2, "known": false, "type": "V", "unit": "second"}}, "edges": {"1": {"origin": 1, "target": 0, "weight": 2}, "3": {"origin": 2, "target": 0, "weight": 2}, "2": {"origin": 3, "target": 0, "weight": 2}}}	$$ L = vT $$
4	Accelerated Motion	{"nodes": {"1": {"xpos": 2, "type": "E", "ypos": 2}, "3": {"xpos": 2, "SolutionVar": false, "known": false, "varName": "v0", "type": "V", "ypos": 1, "unit": "meter / second"}, "2": {"xpos": 1, "SolutionVar": false, "known": false, "varName": "v1", "type": "V", "ypos": 2, "unit": "meter / second"}, "5": {"xpos": 3, "type": "MG", "ypos": 2}, "4": {"xpos": 4, "SolutionVar": false, "known": false, "varName": "T", "type": "V", "ypos": 3, "unit": "hour"}, "6": {"xpos": 4, "varName": "a", "ypos": 1, "type": "V", "unit": "meter / s / s"}}, "edges": {"1": {"origin": 3, "target": 1, "weight": 1.0}, "3": {"origin": 5, "target": 1, "weight": 1.0}, "2": {"origin": 2, "target": 1, "weight": -1.0}, "5": {"origin": 6, "target": 5, "weight": 1.0}, "4": {"origin": 4, "target": 5, "weight": 1.0}}}	{"nodes": {"0": {"xpos": 2, "skillName": "Accelerated Motion", "ypos": 2, "type": "SKILL", "skillEQ": "v1 = v0 + a * T", "skillID": 4}, "3": {"xpos": 1, "SolutionVar": false, "varName": "v0", "ypos": 1, "skillVarLink": 3, "known": false, "type": "V", "unit": "meter / second"}, "2": {"xpos": 2, "SolutionVar": false, "varName": "v1", "ypos": 1, "skillVarLink": 2, "known": false, "type": "V", "unit": "meter / second"}, "4": {"xpos": 3, "SolutionVar": false, "varName": "T", "ypos": 1, "skillVarLink": 4, "known": false, "type": "V", "unit": "hour"}, "6": {"xpos": 4, "varName": "a", "ypos": 1, "skillVarLink": 6, "type": "V", "unit": "meter / s / s"}}, "edges": {"1": {"origin": 3, "target": 0, "weight": 2}, "3": {"origin": 4, "target": 0, "weight": 2}, "2": {"origin": 2, "target": 0, "weight": 2}, "4": {"origin": 6, "target": 0, "weight": 2}}}	$$ v_1 = v_0 + aT $$
5	Accelerated Motion	{"nodes": {"11": {"xpos": 3, "unit": "dimensionless", "varName": "2", "type": "C", "ypos": 4, "value": 2.0}, "10": {"xpos": 3, "type": "PG", "ypos": 3, "power": 11}, "1": {"xpos": 2, "type": "E", "ypos": 2}, "3": {"xpos": 3, "SolutionVar": false, "known": false, "varName": "v0", "type": "V", "ypos": 1, "unit": "meter / second"}, "2": {"xpos": 1, "SolutionVar": false, "known": false, "varName": "x1", "type": "V", "ypos": 2, "unit": "meter"}, "5": {"xpos": 3, "type": "MG", "ypos": 2}, "4": {"xpos": 4, "SolutionVar": false, "known": false, "varName": "T", "type": "V", "ypos": 2, "unit": "hour"}, "7": {"xpos": 2, "varName": "x0", "ypos": 1, "type": "V", "unit": "meter"}, "6": {"xpos": 2, "varName": "a", "ypos": 4, "type": "V", "unit": "meter / s / s"}, "9": {"xpos": 2, "type": "MG", "ypos": 3}, "8": {"xpos": 1, "unit": "dimensionless", "varName": "1/2", "type": "C", "ypos": 3, "value": 0.5}}, "edges": {"11": {"origin": 6, "target": 9, "weight": 1.0}, "10": {"origin": 8, "target": 9, "weight": 1.0}, "1": {"origin": 11, "PI": true, "target": 10, "weight": 1.0}, "3": {"origin": 9, "target": 1, "weight": 1.0}, "2": {"origin": 4, "target": 10, "weight": 1.0}, "5": {"origin": 5, "target": 1, "weight": 1.0}, "4": {"origin": 2, "target": 1, "weight": -1.0}, "7": {"origin": 3, "target": 5, "weight": 1.0}, "6": {"origin": 7, "target": 1, "weight": 1.0}, "9": {"origin": 10, "target": 9, "weight": 1.0}, "8": {"origin": 4, "target": 5, "weight": 1.0}}}	{"nodes": {"0": {"xpos": 2, "skillName": "Accelerated Motion", "ypos": 2, "type": "SKILL", "skillEQ": "x1 = x0 + v0T + 0.5 * aT^2)", "skillID": 5}, "3": {"xpos": 1, "SolutionVar": false, "varName": "v0", "ypos": 1, "skillVarLink": 3, "known": false, "type": "V", "unit": "meter / second"}, "2": {"xpos": 2, "SolutionVar": false, "varName": "x1", "ypos": 1, "skillVarLink": 2, "known": false, "type": "V", "unit": "meter"}, "4": {"xpos": 3, "SolutionVar": false, "varName": "T", "ypos": 1, "skillVarLink": 4, "known": false, "type": "V", "unit": "hour"}, "7": {"xpos": 4, "varName": "x0", "ypos": 1, "skillVarLink": 7, "type": "V", "unit": "meter"}, "6": {"xpos": 5, "varName": "a", "ypos": 1, "skillVarLink": 6, "type": "V", "unit": "meter / s / s"}}, "edges": {"1": {"origin": 3, "target": 0, "weight": 2}, "3": {"origin": 4, "target": 0, "weight": 2}, "2": {"origin": 2, "target": 0, "weight": 2}, "5": {"origin": 6, "target": 0, "weight": 2}, "4": {"origin": 7, "target": 0, "weight": 2}}}	$$ x_1 = x_0 + v_0T + \\frac{1}{2}aT^2 $$
6	Accelerated Motion	{"nodes": {"10": {"xpos": 3, "unit": "dimensionless", "varName": "2", "type": "C", "ypos": 4, "value": 2.0}, "1": {"xpos": 1, "SolutionVar": false, "known": false, "varName": "L", "type": "V", "ypos": 2, "unit": "meter"}, "3": {"xpos": 3, "SolutionVar": false, "known": false, "varName": "v0", "type": "V", "ypos": 1, "unit": "meter / second"}, "2": {"xpos": 2, "type": "E", "ypos": 2}, "5": {"xpos": 3, "type": "MG", "ypos": 2}, "4": {"xpos": 4, "SolutionVar": false, "known": false, "varName": "T", "type": "V", "ypos": 2, "unit": "hour"}, "7": {"xpos": 1, "unit": "dimensionless", "varName": "1/2", "type": "C", "ypos": 3, "value": 0.5}, "6": {"xpos": 2, "varName": "a", "ypos": 4, "type": "V", "unit": "meter / s / s"}, "9": {"xpos": 3, "type": "PG", "ypos": 3, "power": 10}, "8": {"xpos": 2, "type": "MG", "ypos": 3}}, "edges": {"10": {"origin": 6, "target": 8, "weight": 1.0}, "1": {"origin": 1, "target": 2, "weight": -1.0}, "3": {"origin": 5, "target": 2, "weight": 1.0}, "2": {"origin": 8, "target": 2, "weight": 1.0}, "5": {"origin": 4, "target": 5, "weight": 1.0}, "4": {"origin": 3, "target": 5, "weight": 1.0}, "7": {"origin": 4, "target": 9, "weight": 1.0}, "6": {"origin": 10, "PI": true, "target": 9, "weight": 1.0}, "9": {"origin": 7, "target": 8, "weight": 1.0}, "8": {"origin": 9, "target": 8, "weight": 1.0}}}	{"nodes": {"1": {"xpos": 1, "SolutionVar": false, "varName": "L", "ypos": 1, "skillVarLink": 1, "known": false, "type": "V", "unit": "meter"}, "0": {"xpos": 2, "skillName": "Accelerated Motion", "ypos": 2, "type": "SKILL", "skillEQ": "L = v0T + 0.5 * aT^2", "skillID": 6}, "3": {"xpos": 2, "SolutionVar": false, "varName": "v0", "ypos": 1, "skillVarLink": 3, "known": false, "type": "V", "unit": "meter / second"}, "4": {"xpos": 3, "SolutionVar": false, "varName": "T", "ypos": 1, "skillVarLink": 4, "known": false, "type": "V", "unit": "hour"}, "6": {"xpos": 4, "varName": "a", "ypos": 1, "skillVarLink": 6, "type": "V", "unit": "meter / s / s"}}, "edges": {"1": {"origin": 1, "target": 0, "weight": 2}, "3": {"origin": 4, "target": 0, "weight": 2}, "2": {"origin": 3, "target": 0, "weight": 2}, "4": {"origin": 6, "target": 0, "weight": 2}}}	$$ L = v_0T + \\frac{1}{2} aT^2 $$
7	Accelerated Motion	{"nodes": {"1": {"xpos": 1, "SolutionVar": false, "known": false, "varName": "L", "type": "V", "ypos": 1, "unit": "meter"}, "3": {"xpos": 3, "SolutionVar": false, "known": false, "varName": "T", "type": "V", "ypos": 1, "unit": "hour"}, "2": {"xpos": 2, "type": "E", "ypos": 1}, "5": {"xpos": 1, "unit": "dimensionless", "varName": "1/2", "type": "C", "ypos": 2, "value": 0.5}, "4": {"xpos": 2, "varName": "a", "ypos": 3, "type": "V", "unit": "meter / s / s"}, "7": {"xpos": 3, "type": "PG", "ypos": 2, "power": 8}, "6": {"xpos": 2, "type": "MG", "ypos": 2}, "8": {"xpos": 3, "unit": "dimensionless", "varName": "2", "type": "C", "ypos": 3, "value": 2.0}}, "edges": {"1": {"origin": 1, "target": 2, "weight": -1.0}, "3": {"origin": 8, "PI": true, "target": 7, "weight": 1.0}, "2": {"origin": 6, "target": 2, "weight": 1.0}, "5": {"origin": 5, "target": 6, "weight": 1.0}, "4": {"origin": 3, "target": 7, "weight": 1.0}, "7": {"origin": 7, "target": 6, "weight": 1.0}, "6": {"origin": 4, "target": 6, "weight": 1.0}}}	{"nodes": {"1": {"xpos": 1, "SolutionVar": false, "varName": "L", "ypos": 1, "skillVarLink": 1, "known": false, "type": "V", "unit": "meter"}, "0": {"xpos": 2, "skillName": "Accelerated Motion", "ypos": 2, "type": "SKILL", "skillEQ": "L=0.5 * aT^2", "skillID": 7}, "3": {"xpos": 2, "SolutionVar": false, "varName": "T", "ypos": 1, "skillVarLink": 3, "known": false, "type": "V", "unit": "hour"}, "4": {"xpos": 3, "varName": "a", "ypos": 1, "skillVarLink": 4, "type": "V", "unit": "meter / s / s"}}, "edges": {"1": {"origin": 1, "target": 0, "weight": 2}, "3": {"origin": 4, "target": 0, "weight": 2}, "2": {"origin": 3, "target": 0, "weight": 2}}}	$$ L=\\frac{1}{2} aT^2 $$
8	ДИМА ГЕНИЙ	{"edges": {"8": {"origin": 10, "target": 13, "weight": 1}, "9": {"origin": 11, "target": 13, "weight": 1}, "10": {"origin": 13, "target": 12, "weight": 1}, "11": {"origin": 9, "target": 12, "weight": -1}, "12": {"origin": 14, "target": 13, "weight": 1}}, "nodes": {"9": {"state": "unknown", "type": "V", "unit": "N", "value": "", "varName": "F", "xpos": 1, "ypos": 5}, "10": {"state": "unknown", "type": "V", "unit": "kg", "value": "", "varName": "m", "xpos": 6, "ypos": 4}, "11": {"state": "unknown", "type": "V", "unit": "m / s**2", "value": "", "varName": "a", "xpos": 7, "ypos": 6}, "12": {"type": "E", "xpos": 3, "ypos": 5}, "13": {"type": "MG", "xpos": 5, "ypos": 5}, "14": {"type": "V", "xpos": 5, "ypos": 7, "varName": "k", "unit": "", "value": "", "state": "unknown"}}}	{"edges": {"1": {"origin": 9, "target": 0, "weight": 1}, "2": {"origin": 10, "target": 0, "weight": 1}, "3": {"origin": 11, "target": 0, "weight": 1}}, "nodes": {"0": {"skillEQ": "$$ F=ma $$", "skillID": "8", "skillName": "ДИМА ГЕНИЙ", "type": "SKILL", "xpos": 2, "ypos": 2}, "9": {"skillVarLink": 9, "state": "unknown", "type": "V", "unit": "N", "value": "", "varName": "F", "xpos": 1, "ypos": 1}, "10": {"skillVarLink": 10, "state": "unknown", "type": "V", "unit": "kg", "value": "", "varName": "m", "xpos": 2, "ypos": 1}, "11": {"skillVarLink": 11, "state": "unknown", "type": "V", "unit": "m / s**2", "value": "", "varName": "a", "xpos": 2, "ypos": 3}}}	$$ F=ma $$
\.


--
-- Data for Name: user_progress; Type: TABLE DATA; Schema: public; Owner: physai_admin
--

COPY public.user_progress (id, user_id, bundle_id, progress) FROM stdin;
1	9	1	7
3	1	1	0
2	2	1	1
4	2	2	0
5	3	1	0
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: physai_admin
--

COPY public.users (id, username, password, access, email, firstname, lastname, birthdate, country) FROM stdin;
1	dima_admin	$5$rounds=535000$h88vG03c36TOgGYw$vaX76g.M18B5aA/2dEBTKlleROTcCpS3nBuh0hSFGmB	3	dima.ashkinadze@gmail.com	Dzmitry	Ashkinadze	1994-05-15	Switzerland
9	dima	$5$rounds=535000$h88vG03c36TOgGYw$vaX76g.M18B5aA/2dEBTKlleROTcCpS3nBuh0hSFGmB	2	dima.ashkinadze@gmail.com	Dzmitry	Ashkinadze	1994-05-15	Switzerland
10	dima_basic	$5$rounds=535000$h88vG03c36TOgGYw$vaX76g.M18B5aA/2dEBTKlleROTcCpS3nBuh0hSFGmB	1	dima.ashkinadze@gmail.com	Dzmitry	Ashkinadze	1994-05-15	Switzerland
2	Anton	$5$rounds=535000$w1BYM4a3J2oAJwu4$dfkBuhN2d0dm5K9Jq904WmeLBMHHlxZwhEM3OLvpYe/	1	aad362@mail.ru	Anton	Ash	1969-12-09	Belarus
3	Nastyshik	$5$rounds=535000$pfUCTKWHfEiCP4kU$pwUVW1hoPZy.It77e52Nn6eh8byBVNn3LoRNBZiT8g5	1	anastasia.ashkinadze@gmail.com	Anastasiia	Ashkinadze	1994-07-23	Russia
\.


--
-- Name: bundles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: physai_admin
--

SELECT pg_catalog.setval('public.bundles_id_seq', 1, false);


--
-- Name: problem_skills_id_seq; Type: SEQUENCE SET; Schema: public; Owner: physai_admin
--

SELECT pg_catalog.setval('public.problem_skills_id_seq', 1, false);


--
-- Name: problems_id_seq; Type: SEQUENCE SET; Schema: public; Owner: physai_admin
--

SELECT pg_catalog.setval('public.problems_id_seq', 1, false);


--
-- Name: skills_id_seq; Type: SEQUENCE SET; Schema: public; Owner: physai_admin
--

SELECT pg_catalog.setval('public.skills_id_seq', 1, false);


--
-- Name: user_progress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: physai_admin
--

SELECT pg_catalog.setval('public.user_progress_id_seq', 5, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: physai_admin
--

SELECT pg_catalog.setval('public.users_id_seq', 3, true);


--
-- Name: bundles bundles_pkey; Type: CONSTRAINT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.bundles
    ADD CONSTRAINT bundles_pkey PRIMARY KEY (id);


--
-- Name: problem_skills problem_skills_pkey; Type: CONSTRAINT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.problem_skills
    ADD CONSTRAINT problem_skills_pkey PRIMARY KEY (id);


--
-- Name: problems problems_pkey; Type: CONSTRAINT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.problems
    ADD CONSTRAINT problems_pkey PRIMARY KEY (id);


--
-- Name: skills skills_pkey; Type: CONSTRAINT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.skills
    ADD CONSTRAINT skills_pkey PRIMARY KEY (id);


--
-- Name: user_progress user_progress_pkey; Type: CONSTRAINT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.user_progress
    ADD CONSTRAINT user_progress_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: problems fk_bundle; Type: FK CONSTRAINT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.problems
    ADD CONSTRAINT fk_bundle FOREIGN KEY (bundle_id) REFERENCES public.bundles(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: user_progress fk_bundle; Type: FK CONSTRAINT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.user_progress
    ADD CONSTRAINT fk_bundle FOREIGN KEY (bundle_id) REFERENCES public.bundles(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: problem_skills fk_problem; Type: FK CONSTRAINT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.problem_skills
    ADD CONSTRAINT fk_problem FOREIGN KEY (problem_id) REFERENCES public.problems(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: problem_skills fk_skill; Type: FK CONSTRAINT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.problem_skills
    ADD CONSTRAINT fk_skill FOREIGN KEY (skill_id) REFERENCES public.skills(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: user_progress fk_user; Type: FK CONSTRAINT; Schema: public; Owner: physai_admin
--

ALTER TABLE ONLY public.user_progress
    ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES public.users(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: physai_admin
--

REVOKE ALL ON SCHEMA public FROM rdsadmin;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO physai_admin;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

