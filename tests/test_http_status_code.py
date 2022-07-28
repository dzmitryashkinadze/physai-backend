import os
import pytest
from turtle import end_fill
import json
from flask_sqlalchemy import SQLAlchemy


def test_login(client, helpers):
    """Make sure login and logout works."""
    rv = helpers.login(client, 'admin', 'admin')
    assert 'Login granted' == json.loads(rv.data.decode('utf8'))['message']
    rv = helpers.login(client, 'adminx', 'admin')
    assert 'Bad username or password' == json.loads(rv.data.decode('utf8'))['message']
    rv = helpers.login(client, 'admin', 'adminx')
    assert 'Bad username or password' == json.loads(rv.data.decode('utf8'))['message']

def test_endpoints_get_AL0(client):
    # open endpoints (AL=0)
    assert client.get('/api/bundles').status_code == 200
    assert client.get('/api/skills').status_code == 200
    # private endpoints (AL=1), only to registered users
    assert client.get('/api/problem_skills/1').status_code == 401
    assert client.get('/api/problems/1').status_code == 401
    assert client.get('/api/bundle/1').status_code == 401
    assert client.get('/api/skill/1').status_code == 401
    assert client.get('/api/problem/1').status_code == 401
    assert client.get('/api/validate').status_code == 401
    assert client.get('/api/user/1').status_code == 401
    assert client.get('/api/user_progress/1').status_code == 401
    assert client.get('/api/user_progress_all').status_code == 401
    # admin accessable endpoints (AL=3)
    assert client.get('/api/admin/bundles').status_code == 401
    assert client.get('/api/admin/problems/1').status_code == 401
    assert client.get('/api/users').status_code == 401
    # endpoints that dont have a get method defined
    assert client.get('/api/register').status_code == 405
    assert client.get('/api/login').status_code == 405
    assert client.get('/api/admin_login').status_code == 405
    assert client.get('/api/refresh_token').status_code == 405

def test_endpoints_get_AL1(client, helpers):
    # login as admin
    rv = helpers.login(client, 'admin', 'admin')
    assert rv.status_code == 200
    access_token = json.loads(rv.data.decode('utf8'))['access_token']
    # create a test user with access level 1
    rv = helpers.create_test_user(client)
    assert rv.status_code == 200
    # login as user
    rv = helpers.login(client, 'user', 'user')
    assert rv.status_code == 200
    responce_dict = json.loads(rv.data.decode('utf8'))
    access_token = responce_dict['access_token']
    user_id = responce_dict['user_id']
    # open endpoints (AL=0)
    assert helpers.private_api_get(client, '/api/bundles', access_token).status_code == 200
    assert helpers.private_api_get(client, '/api/skills', access_token).status_code == 200
    # private endpoints (AL=1)
    assert helpers.private_api_get(client, '/api/validate', access_token).status_code == 200
    assert helpers.private_api_get(client, '/api/user/' + str(user_id), access_token).status_code == 200
    assert helpers.private_api_get(client, '/api/user_progress_all', access_token).status_code == 200
    assert helpers.private_api_get(client, '/api/problem_skills/1', access_token).status_code == 200
    assert helpers.private_api_get(client, '/api/problems/1', access_token).status_code == 200
    # private endpoints for non-existing resources
    assert helpers.private_api_get(client, '/api/bundle/1', access_token).status_code == 404
    assert helpers.private_api_get(client, '/api/skill/1', access_token).status_code == 404
    assert helpers.private_api_get(client, '/api/problem/1', access_token).status_code == 404
    # admin endpoints (AL=3)
    assert helpers.private_api_get(client, '/api/admin/bundles', access_token).status_code == 401
    assert helpers.private_api_get(client, '/api/users', access_token).status_code == 401
    assert helpers.private_api_get(client, '/api/admin/problems/1', access_token).status_code == 401
    # endpoints that dont have a get method defined
    assert helpers.private_api_get(client, '/api/register', access_token).status_code == 405
    assert helpers.private_api_get(client, '/api/login', access_token).status_code == 405
    assert helpers.private_api_get(client, '/api/admin_login', access_token).status_code == 405
    assert helpers.private_api_get(client, '/api/refresh_token', access_token).status_code == 405
    # login as admin
    rv = helpers.login(client, 'admin', 'admin')
    assert rv.status_code == 200
    access_token = json.loads(rv.data.decode('utf8'))['access_token']
    # delete test user
    rv = helpers.delete_test_user(client, user_id, access_token)
    assert rv.status_code == 200

def test_endpoints_get_AL3(client, helpers):
    # logind
    rv = helpers.login(client, 'admin', 'admin')
    assert rv.status_code == 200
    responce_dict = json.loads(rv.data.decode('utf8'))
    access_token = responce_dict['access_token']
    user_id = responce_dict['user_id']
    # open endpoints (AL=0)
    assert helpers.private_api_get(client, '/api/bundles', access_token).status_code == 200
    assert helpers.private_api_get(client, '/api/skills', access_token).status_code == 200
    # private endpoints (AL=1), only to registered users
    assert helpers.private_api_get(client, '/api/validate', access_token).status_code == 200
    # you can access user info only about yourself
    assert helpers.private_api_get(client, '/api/user/' + str(user_id), access_token).status_code == 200
    assert helpers.private_api_get(client, '/api/user_progress_all', access_token).status_code == 200
    assert helpers.private_api_get(client, '/api/problem_skills/1', access_token).status_code == 200
    assert helpers.private_api_get(client, '/api/problems/1', access_token).status_code == 200
    # private endpoints for non-existing resources
    assert helpers.private_api_get(client, '/api/bundle/1', access_token).status_code == 404
    assert helpers.private_api_get(client, '/api/skill/1', access_token).status_code == 404
    assert helpers.private_api_get(client, '/api/problem/1', access_token).status_code == 404
    # admin endpoints (AL=3)
    assert helpers.private_api_get(client, '/api/admin/bundles', access_token).status_code == 200
    assert helpers.private_api_get(client, '/api/users', access_token).status_code == 200
    assert helpers.private_api_get(client, '/api/admin/problems/1', access_token).status_code == 200
    # endpoints that dont have a get method defined
    assert helpers.private_api_get(client, '/api/register', access_token).status_code == 405
    assert helpers.private_api_get(client, '/api/login', access_token).status_code == 405
    assert helpers.private_api_get(client, '/api/admin_login', access_token).status_code == 405
    assert helpers.private_api_get(client, '/api/refresh_token', access_token).status_code == 405