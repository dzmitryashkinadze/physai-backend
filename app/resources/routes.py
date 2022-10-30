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

# user recource classes
from app.resources.user.register import UserRegister
from app.resources.user.user_login import UserLogin
from app.resources.user.validate import UserValidate
from app.resources.user.refresh_token import UserRefreshToken
from app.resources.user.course import CourseList
from app.resources.user.course import Course
from app.resources.user.lesson import Lesson
from app.resources.user.email import Email

# admin resource classes
from app.resources.admin.login import AdminLogin
from app.resources.admin.validate import AdminValidate
from app.resources.admin.refresh_token import AdminRefreshToken
from app.resources.admin.chapter import AdminChapter, AdminChapterList
from app.resources.admin.concept import AdminConcept, AdminConceptList
from app.resources.admin.course import AdminCourse, AdminCourseList
from app.resources.admin.equation import AdminEquation, AdminEquationList
from app.resources.admin.frame import AdminFrame, AdminFrameList
from app.resources.admin.group import AdminGroup, AdminGroupList
from app.resources.admin.lesson import AdminLesson, AdminLessonList
from app.resources.admin.mcq_choice import AdminMCQChoice, AdminMCQChoiceList
from app.resources.admin.mcq import AdminMCQ, AdminMCQList
from app.resources.admin.problem import AdminProblem, AdminProblemList
from app.resources.admin.tag import AdminTag, AdminTagList
from app.resources.admin.test import AdminTest, AdminTestList
from app.resources.admin.user_active import AdminUserActive, AdminUserActiveList
from app.resources.admin.user_detail import AdminUserDetail, AdminUserDetailList
from app.resources.admin.user_feedback import AdminUserFeedback, AdminUserFeedbackList
from app.resources.admin.user_login import AdminUserLogin, AdminUserLoginList
from app.resources.admin.user_progress_course import AdminUserProgressCourse, AdminUserProgressCourseList
from app.resources.admin.user_progress_lesson import AdminUserProgressLesson, AdminUserProgressLessonList
from app.resources.admin.user_rating import AdminUserRating, AdminUserRatingList
from app.resources.admin.user import AdminUser, AdminUserList
from app.resources.admin.image import AdminImage, AdminImageList


def initialize_routes(api, image_bucket, ses_client):

    #############################
    ###### USER ENDPOINTS ######
    #############################
    # Authorization endpoints
    api.add_resource(UserRegister, '/api/register')
    api.add_resource(UserLogin, '/api/login')
    api.add_resource(UserValidate, '/api/validate')
    api.add_resource(UserRefreshToken, '/api/refresh_token')
    # Utillity endpoints
    api.add_resource(Email, '/api/email',
                     resource_class_args=(ses_client,))
    # Frontend pages
    api.add_resource(CourseList, '/api/page_courses')
    api.add_resource(Course, '/api/page_course/<string:id>')
    api.add_resource(Lesson, '/api/page_lesson/<string:id>')

    #############################
    ###### ADMIN ENDPOINTS ######
    #############################
    # Authorization endpoints
    api.add_resource(AdminLogin, '/api/admin/login')
    api.add_resource(AdminValidate, '/api/admin/validate')
    api.add_resource(AdminRefreshToken, '/api/admin/refresh_token')
    # Resource groups
    api.add_resource(AdminChapter, '/api/admin/chapters/<string:id>')
    api.add_resource(AdminChapterList, '/api/admin/chapters')
    api.add_resource(AdminConcept, '/api/admin/concepts/<string:id>')
    api.add_resource(AdminConceptList, '/api/admin/concepts')
    api.add_resource(AdminCourse, '/api/admin/courses/<string:id>')
    api.add_resource(AdminCourseList, '/api/admin/courses')
    api.add_resource(AdminEquation, '/api/admin/equations/<string:id>')
    api.add_resource(AdminEquationList, '/api/admin/equations')
    api.add_resource(AdminFrame, '/api/admin/frames/<string:id>')
    api.add_resource(AdminFrameList, '/api/admin/frames')
    api.add_resource(AdminGroup, '/api/admin/groups/<string:id>')
    api.add_resource(AdminGroupList, '/api/admin/groups')
    api.add_resource(AdminLesson, '/api/admin/lessons/<string:id>')
    api.add_resource(AdminLessonList, '/api/admin/lessons')
    api.add_resource(AdminMCQChoice, '/api/admin/mcq_choices/<string:id>')
    api.add_resource(AdminMCQChoiceList, '/api/admin/mcq_choices')
    api.add_resource(AdminMCQ, '/api/admin/mcqs/<string:id>')
    api.add_resource(AdminMCQList, '/api/admin/mcqs')
    api.add_resource(AdminProblem, '/api/admin/problems/<string:id>')
    api.add_resource(AdminProblemList, '/api/admin/problems')
    api.add_resource(AdminTag, '/api/admin/tags/<string:id>')
    api.add_resource(AdminTagList, '/api/admin/tags')
    api.add_resource(AdminTest, '/api/admin/tests/<string:id>')
    api.add_resource(AdminTestList, '/api/admin/tests')
    api.add_resource(AdminUserActive, '/api/admin/user_actives/<string:id>')
    api.add_resource(AdminUserActiveList, '/api/admin/user_actives')
    api.add_resource(AdminUserDetail, '/api/admin/user_details/<string:id>')
    api.add_resource(AdminUserDetailList, '/api/admin/user_details')
    api.add_resource(AdminUserFeedback,
                     '/api/admin/user_feedbacks/<string:id>')
    api.add_resource(AdminUserFeedbackList, '/api/admin/user_feedbacks')
    api.add_resource(AdminUserLogin, '/api/admin/user_logins/<string:id>')
    api.add_resource(AdminUserLoginList, '/api/admin/user_logins')
    api.add_resource(AdminUserProgressCourse,
                     '/api/admin/user_progress_courses/<string:id>')
    api.add_resource(AdminUserProgressCourseList,
                     '/api/admin/user_progress_courses')
    api.add_resource(AdminUserProgressLesson,
                     '/api/admin/user_progress_lessons/<string:id>')
    api.add_resource(AdminUserProgressLessonList,
                     '/api/admin/user_progress_lessons')
    api.add_resource(AdminUserRating, '/api/admin/user_ratings/<string:id>')
    api.add_resource(AdminUserRatingList, '/api/admin/user_ratings')
    api.add_resource(AdminUser, '/api/admin/users/<string:id>')
    api.add_resource(AdminUserList, '/api/admin/users')
    api.add_resource(AdminImage, '/api/admin/images/<string:key>',
                     resource_class_args=(image_bucket,))
    api.add_resource(AdminImageList, '/api/admin/images',
                     resource_class_args=(image_bucket,))
