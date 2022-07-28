import json
import pytest


def test_user_recycling(client, helpers):
    
    # login as admin
    rv = helpers.login(client, 'test', 'test')
    assert 'message' in dict(json.loads(rv.data.decode('utf8'))).keys()
    assert json.loads(rv.data.decode('utf8'))['message'] == 'Bad username or password'
    assert 'status' in dict(json.loads(rv.data.decode('utf8'))).keys()
    assert json.loads(rv.data.decode('utf8'))['status'] == 1