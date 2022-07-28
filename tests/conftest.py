from cgitb import reset
import os
from re import U
from turtle import end_fill
from numpy import fix
import pytest
from models.user import UserModel
from config import TestConfig


# import the flask app
from app import create_app, db
# import models

@pytest.fixture(scope='session', autouse=True)
def client():
    app = create_app(TestConfig)
    app_context = app.app_context()
    app_context.push()
    db.create_all()
    yield app.test_client()  # tests run here
    db.drop_all()  # drop all tables

class Helpers:
    @staticmethod
    # Login helper function
    def login(client, username, password):
        return client.post(
            "/api/login",
            data=dict(username=username, password=password)
        )

    # Helper function for creation of a test user
    @staticmethod
    def create_test_user(client):
        return client.post(
            '/api/register',
            data = {
                'username':'user',
                'email':'test_user',
                'firstname':'user',
                'lastname':'user',
                'birthdate':'test',
                'country':'test',
                'password':'user'
            }
        )

    # Helper function for deletion of a test user
    @staticmethod
    def delete_test_user(client, user_id, access_token):
        return client.delete(
            '/api/user/' + str(user_id),
            headers={'Authorization':'Bearer {}'.format(access_token)})

    # Helper function for a private api request
    @staticmethod
    def private_api_get(client, uri, access_token):
        return client.get(
            uri,
            headers={'Authorization':'Bearer {}'.format(access_token)})

@pytest.fixture
def helpers():
    return Helpers()