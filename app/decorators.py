from app.models.user import UserModel
from functools import wraps
from flask import request, current_app
import jwt

def auth_required(access=1):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                auth_header = request.headers.get('authorization')
            if auth_header:
                token = auth_header.split(" ")[1] # Parses out the "Bearer" portion
            else:
                token = ''
            if token:
                try:
                    decoded = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
                except jwt.ExpiredSignatureError:
                    return {'message': 'token expired',
                            'auth': 0}, 401
                except jwt.InvalidTokenError:
                    return {'message': 'token invalid',
                            'auth': 0}, 401
                if not isinstance(decoded, str):
                    user = UserModel.find_by_email(decoded['email'])
                    if not user:
                        return {'message': 'token invalid',
                                'auth': 0}, 401
                    elif int(user.access) < access:
                        return {'message': 'permission denied',
                                'auth': 0}, 401
                    else:
                        return f(user, *args, **kwargs)
                else:
                    return {'message': 'token invalid',
                            'auth': 0}, 401
            return {'message': 'token missing',
                    'auth': 0}, 401
        return wrapper
    return decorator

# def auth_required(f):
#     @wraps(f)
#     def wrapper(*args, **kwargs):
#         auth_header = request.headers.get('Authorization')
#         if auth_header:
#             token = auth_header.split(" ")[1] # Parses out the "Bearer" portion
#         else:
#             token = ''
#         if token:
#             try:
#                 decoded = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
#             except jwt.ExpiredSignatureError:
#                 return {'message': 'token expired',
#                         'auth': 0}, 401
#             except jwt.InvalidTokenError:
#                 return {'message': 'token invalid',
#                         'auth': 0}, 401
#             if not isinstance(decoded, str):
#                 user = UserModel.find_by_username(decoded['name'])
#                 if not user:
#                     return {'message': 'token invalid',
#                             'auth': 0}, 401
#                 elif int(user.access) < 1:
#                     return {'message': 'permission denied',
#                             'auth': 0}, 401
#                 else:
#                     return f(user, *args, **kwargs)
#             else:
#                 return {'message': 'token invalid',
#                         'auth': 0}, 401
#         return {'message': 'token missing',
#                 'auth': 0}, 401
#     return wrapper
