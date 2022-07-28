# recources (api calls)
from app.resources.bundle import Bundle, BundleList, BundleListAdmin
from app.resources.skill import Skill, SkillList
from app.resources.problemskill import ProblemSkillList
from app.resources.problem import Problem, ProblemList, ProblemListAdmin
from app.resources.user import User
from app.resources.user import UserRegister
from app.resources.user import UserLogin
from app.resources.user import UserRefresh
from app.resources.user import UserValidate
from app.resources.user import AdminLogin
from app.resources.user import UserList
from app.resources.user_progress import UserProgress, UserProgressList
from app.resources.image import Image, ImageList


def initialize_routes(api):
    # list of endpoints
    api.add_resource(Bundle, '/api/bundle/<string:id>')
    api.add_resource(BundleList, '/api/bundles')
    api.add_resource(BundleListAdmin, '/api/admin/bundles')
    api.add_resource(Skill, '/api/skill/<string:id>')
    api.add_resource(ProblemSkillList, '/api/problem_skills/<string:problem_id>')
    api.add_resource(SkillList, '/api/skills')
    api.add_resource(Problem, '/api/problem/<string:id>')
    api.add_resource(ProblemList, '/api/problems/<string:bundle_id>')
    api.add_resource(ProblemListAdmin, '/api/admin/problems/<string:bundle_id>')
    api.add_resource(UserRegister, '/api/register')
    api.add_resource(UserLogin, '/api/login')
    api.add_resource(AdminLogin, '/api/admin_login')
    api.add_resource(UserRefresh, '/api/refresh_token')
    api.add_resource(UserList, '/api/users')
    api.add_resource(UserValidate, '/api/validate')
    api.add_resource(User, '/api/user/<string:id>')
    api.add_resource(UserProgress, '/api/user_progress/<string:id>')
    api.add_resource(UserProgressList, '/api/user_progress_all')
    api.add_resource(Image, '/api/image/<string:key>')
    api.add_resource(ImageList, '/api/images')
