'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'lucky'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjUzODg4MDgsIm5iZiI6MTY2NDE3OTIwOCwiZW1haWwiOiJsdWNreUBnbWFpbC5jb20ifQ.EFVmNS8FpKw8vilSmq-ZeSPL3W8cnqmdajQK4k6Y7e4'
EMAIL = 'lucky@gmail.com'
PASSWORD = 'Goodboylucky123'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'
    # assert False


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
