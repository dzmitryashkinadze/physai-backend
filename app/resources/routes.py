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
from app.resources.admin.course import AdminCourse, AdminCourseList
from app.resources.admin.equation import AdminEquation, AdminEquationList
from app.resources.admin.problem import AdminProblem, AdminProblemList
from app.resources.admin.user import AdminUser, AdminUserList
from app.resources.admin.image import AdminImage, AdminImageList


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
    api.add_resource(AdminCourse, "/api/admin/courses/<string:id>")
    api.add_resource(AdminCourseList, "/api/admin/courses")
    api.add_resource(AdminEquation, "/api/admin/equations/<string:id>")
    api.add_resource(AdminEquationList, "/api/admin/equations")
    api.add_resource(AdminProblem, "/api/admin/problems/<string:id>")
    api.add_resource(AdminProblemList, "/api/admin/problems")
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
