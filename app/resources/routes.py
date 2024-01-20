# user recource classes
from app.resources.user.register import UserRegister
from app.resources.user.login import UserLogin
from app.resources.user.validate import UserValidate
from app.resources.user.refresh_token import UserRefreshToken
from app.resources.user.course import CourseList
from app.resources.user.course import Course

# from app.resources.user.lesson import Lesson
# from app.resources.user.email import Email

# admin resource classes
from app.resources.admin.course_equation import (
    AdminCourseEquation,
    AdminCourseEquationList,
)
from app.resources.admin.course_problem import (
    AdminCourseProblem,
    AdminCourseProblemList,
)
from app.resources.admin.course_tag import AdminCourseTag, AdminCourseTagList
from app.resources.admin.course_theory import AdminCourseTheory, AdminCourseTheoryList
from app.resources.admin.course import AdminCourse, AdminCourseList
from app.resources.admin.equation_tag import AdminEquationTag, AdminEquationTagList
from app.resources.admin.equation import AdminEquation, AdminEquationList
from app.resources.admin.login import AdminLogin
from app.resources.admin.problem_equation import (
    AdminProblemEquation,
    AdminProblemEquationList,
)
from app.resources.admin.problem_tag import AdminProblemTag, AdminProblemTagList
from app.resources.admin.problem import AdminProblem, AdminProblemList
from app.resources.admin.tag import AdminTag, AdminTagList
from app.resources.admin.theory import AdminTheory, AdminTheoryList
from app.resources.admin.user_login import AdminUserLoginList
from app.resources.admin.user_progress_course import AdminUserProgressCourseList
from app.resources.admin.user_progress_problem import AdminUserProgressProblemList
from app.resources.admin.user import AdminUser, AdminUserList


def initialize_routes(api):  # image_bucket, ses_client):
    #############################
    ###### USER ENDPOINTS ######
    #############################
    # Authorization endpoints
    api.add_resource(UserRegister, "/api/register")
    api.add_resource(UserLogin, "/api/login")
    api.add_resource(UserValidate, "/api/validate")
    api.add_resource(UserRefreshToken, "/api/refresh_token")
    # Frontend pages
    api.add_resource(CourseList, "/api/courses")
    api.add_resource(Course, "/api/course/<string:id>")

    #############################
    ###### ADMIN ENDPOINTS ######
    #############################
    # Resource groups
    api.add_resource(AdminCourseEquation, "/api/admin/course_equations/<string:id>")
    api.add_resource(AdminCourseEquationList, "/api/admin/course_equations")
    api.add_resource(AdminCourseProblem, "/api/admin/course_problems/<string:id>")
    api.add_resource(AdminCourseProblemList, "/api/admin/course_problems")
    api.add_resource(AdminCourseTag, "/api/admin/course_tags/<string:id>")
    api.add_resource(AdminCourseTagList, "/api/admin/course_tags")
    api.add_resource(AdminCourseTheory, "/api/admin/course_theories/<string:id>")
    api.add_resource(AdminCourseTheoryList, "/api/admin/course_theories")
    api.add_resource(AdminCourse, "/api/admin/courses/<string:id>")
    api.add_resource(AdminCourseList, "/api/admin/courses")
    api.add_resource(AdminEquationTag, "/api/admin/equation_tags/<string:id>")
    api.add_resource(AdminEquationTagList, "/api/admin/equation_tags")
    api.add_resource(AdminEquation, "/api/admin/equations/<string:id>")
    api.add_resource(AdminEquationList, "/api/admin/equations")
    api.add_resource(AdminLogin, "/api/admin/login")
    api.add_resource(AdminProblemEquation, "/api/admin/problem_equations/<string:id>")
    api.add_resource(AdminProblemEquationList, "/api/admin/problem_equations")
    api.add_resource(AdminProblemTag, "/api/admin/problem_tags/<string:id>")
    api.add_resource(AdminProblemTagList, "/api/admin/problem_tags")
    api.add_resource(AdminProblem, "/api/admin/problems/<string:id>")
    api.add_resource(AdminProblemList, "/api/admin/problems")
    api.add_resource(AdminTag, "/api/admin/tags/<string:id>")
    api.add_resource(AdminTagList, "/api/admin/tags")
    api.add_resource(AdminTheory, "/api/admin/theories/<string:id>")
    api.add_resource(AdminTheoryList, "/api/admin/theories")
    api.add_resource(AdminUserLoginList, "/api/admin/user_logins")
    api.add_resource(AdminUserProgressCourseList, "/api/admin/user_progress_courses")
    api.add_resource(AdminUserProgressProblemList, "/api/admin/user_progress_problems")
    api.add_resource(AdminUser, "/api/admin/users/<string:id>")
    api.add_resource(AdminUserList, "/api/admin/users")
    # api.add_resource(
    #     AdminImage,
    #     "/api/admin/images/<string:key>",
    #     resource_class_args=(image_bucket,),
    # )
    # api.add_resource(
    #     AdminImageList, "/api/admin/images", resource_class_args=(image_bucket,)
    # )
