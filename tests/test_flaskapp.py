# test_flask_app.py
import pytest
from flask_app import app

def test_homepage():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_api_endpoint():
    response = app.test_client().get('/api/data')
    assert response.status_code == 200
    assert 'data' in response.json
