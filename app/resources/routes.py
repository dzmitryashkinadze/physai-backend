# TO BE removed later
from app.models.chapter import ChapterModel
from app.models.concept import ConceptModel
from app.models.course_equation import CourseEquationModel
from app.models.course_tag import CourseTagModel
from app.models.course import CourseModel
from app.models.equation import EquationModel
from app.models.frame import FrameModel
from app.models.group import GroupModel
from app.models.group_course import GroupCourseModel
from app.models.lesson import LessonModel
from app.models.mcq_choice import MCQChoiceModel
from app.models.mcq import MCQModel
from app.models.problem_equation import ProblemEquationModel
from app.models.problem import ProblemModel
from app.models.tag import TagModel
from app.models.user_active import UserActiveModel
from app.models.user_detail import UserDetailModel
from app.models.user_feedback import UserFeedbackModel
from app.models.user_login import UserLoginModel
from app.models.user_progress_course import UserProgressCourseModel
from app.models.user_progress_lesson import UserProgressLessonModel
from app.models.user_rating import UserRatingModel

# recources (api calls)
#from app.resources.bundle import Bundle, BundleList, AdminBundle, AdminBundleList
#from app.resources.skill import Skill, SkillList, AdminSkill, AdminSkillList
#from app.resources.problemskill import ProblemSkillList, AdminProblemSkillList
#from app.resources.problem import Problem, AdminProblem, ProblemList, AdminProblemList
#from app.resources.user import User, AdminUser
#from app.resources.user import UserRegister
#from app.resources.user import UserLogin, AdminLogin
#from app.resources.user import UserRefreshToken, AdminRefreshToken
#from app.resources.user import UserValidate, AdminValidate
#from app.resources.user import AdminUserList
#from app.resources.user_progress import UserProgress, UserProgressList, AdminUserProgress, AdminUserProgressList
#from app.resources.image import AdminImage, AdminImageList
from app.resources.user_register import UserRegister
from app.resources.user_login import UserLogin
from app.resources.user_validate import UserValidate
from app.resources.user_refresh_token import UserRefreshToken


def initialize_routes(api):

    #############################
    ###### USER ENDPOINTS ######
    #############################
    # Authorization endpoints
    api.add_resource(UserRegister, '/api/register')
    api.add_resource(UserLogin, '/api/login')
    api.add_resource(UserValidate, '/api/validate')
    api.add_resource(UserRefreshToken, '/api/refresh_token')
    # Resource: bundle
    #api.add_resource(Bundle, '/api/bundles/<string:id>')
    #api.add_resource(BundleList, '/api/bundles')
    # Resource: user
    #api.add_resource(User, '/api/users/<string:id>')
    # Resource: problem
    #api.add_resource(Problem, '/api/problem/<string:id>')
    #api.add_resource(ProblemList, '/api/problems/<string:bundle_id>')
    # Resource: skill
    #api.add_resource(Skill, '/api/skill/<string:id>')
    #api.add_resource(SkillList, '/api/skills')
    # Resource: problem_skill (relationship)
    #api.add_resource(ProblemSkillList, '/api/problem_skills/<string:problem_id>')
    # Resource: user_progress (relationship)
    #api.add_resource(UserProgress, '/api/user_progress/<string:id>')
    #api.add_resource(UserProgressList, '/api/user_progress_all')
    #############################
    ###### ADMIN ENDPOINTS ######
    #############################
    # Authorization endpoints
    #api.add_resource(AdminLogin, '/api/admin/login')
    #api.add_resource(AdminValidate, '/api/admin/validate')
    #api.add_resource(AdminRefreshToken, '/api/admin/refresh_token')
    # Resource: bundle
    #api.add_resource(AdminBundle, '/api/admin/bundles/<string:id>')
    #api.add_resource(AdminBundleList, '/api/admin/bundles')
    # Resource: user
    #api.add_resource(AdminUserList, '/api/admin/users')
    #api.add_resource(AdminUser, '/api/admin/users/<string:id>')
    # Resource: problem
    #api.add_resource(AdminProblemList, '/api/admin/problems')
    #api.add_resource(AdminProblem, '/api/admin/problems/<string:id>')
    # Resource: skill
    #api.add_resource(AdminSkillList, '/api/admin/skills')
    #api.add_resource(AdminSkill, '/api/admin/skills/<string:id>')
    # TODO: Resource: problem_skill (relationship)
    # api.add_resource(AdminProblemSkillList, '/api/admin/problem_skills/<string:problem_id>')
    # Resource: user_progress (relationship)
    #api.add_resource(AdminUserProgress, '/api/admin/user_progress/<string:id>')
    #api.add_resource(AdminUserProgressList, '/api/admin/user_progress')
    # Route (not DB dependent functions): image
    #api.add_resource(AdminImage, '/api/admin/image/<string:key>')
    # #api.add_resource(AdminImageList, '/api/admin/images')
