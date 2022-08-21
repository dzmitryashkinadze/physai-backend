# recources (api calls)
from app.resources.bundle import Bundle, BundleList, AdminBundle, AdminBundleList
from app.resources.skill import Skill, SkillList, AdminSkill, AdminSkillList
from app.resources.problemskill import ProblemSkillList, AdminProblemSkillList
from app.resources.problem import Problem, AdminProblem, ProblemList, AdminProblemList
from app.resources.user import User, AdminUser
from app.resources.user import UserRegister
from app.resources.user import UserLogin, AdminLogin
from app.resources.user import UserRefreshToken, AdminRefreshToken
from app.resources.user import UserValidate, AdminValidate
from app.resources.user import AdminUserList
from app.resources.user_progress import UserProgress, UserProgressList, AdminUserProgress, AdminUserProgressList
from app.resources.image import AdminImage, AdminImageList


def initialize_routes(api):

    # List of user accessable endpoints
    # Authorization endpoints
    api.add_resource(UserRegister, '/api/register')
    api.add_resource(UserLogin, '/api/login')
    api.add_resource(UserValidate, '/api/validate')
    api.add_resource(UserRefreshToken, '/api/refresh_token')
    # Resource: bundle
    api.add_resource(Bundle, '/api/bundles/<string:id>')
    api.add_resource(BundleList, '/api/bundles')
    # Resource: user
    api.add_resource(User, '/api/users/<string:id>')
    # Resource: problem
    api.add_resource(Problem, '/api/problem/<string:id>')
    api.add_resource(ProblemList, '/api/problems/<string:bundle_id>')
    # Resource: skill
    api.add_resource(Skill, '/api/skill/<string:id>')
    api.add_resource(SkillList, '/api/skills')
    # Resource: problem_skill (relationship)
    api.add_resource(ProblemSkillList, '/api/problem_skills/<string:problem_id>')
    # Resource: user_progress (relationship)
    api.add_resource(UserProgress, '/api/user_progress/<string:id>')
    api.add_resource(UserProgressList, '/api/user_progress_all')
    

    # List of admin endpoints for the admin panel
    # Authorization endpoints
    api.add_resource(AdminLogin, '/api/admin/login')
    api.add_resource(AdminValidate, '/api/admin/validate')
    api.add_resource(AdminRefreshToken, '/api/admin/refresh_token')
    # Resource: bundle
    api.add_resource(AdminBundle, '/api/admin/bundles/<string:id>')
    api.add_resource(AdminBundleList, '/api/admin/bundles')
    # Resource: user
    api.add_resource(AdminUserList, '/api/admin/users')
    api.add_resource(AdminUser, '/api/admin/users/<string:id>')
    # Resource: problem
    api.add_resource(AdminProblemList, '/api/admin/problems')
    api.add_resource(AdminProblem, '/api/admin/problems/<string:id>')
    # Resource: skill
    api.add_resource(AdminSkillList, '/api/admin/skills')
    api.add_resource(AdminSkill, '/api/admin/skills/<string:id>')
    # TODO: Resource: problem_skill (relationship) 
    # api.add_resource(AdminProblemSkillList, '/api/admin/problem_skills/<string:problem_id>')
    # Resource: user_progress (relationship)
    api.add_resource(AdminUserProgress, '/api/admin/user_progress/<string:id>')
    api.add_resource(AdminUserProgressList, '/api/admin/user_progress')
    # Route (not DB dependent functions): image
    api.add_resource(AdminImage, '/api/admin/image/<string:key>')
    api.add_resource(AdminImageList, '/api/admin/images')
