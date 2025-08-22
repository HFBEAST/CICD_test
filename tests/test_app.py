import pytest
import json
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert 'version' in data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_calculate_add(client):
    response = client.post('/calculate',
                          json={'a': 5, 'b': 3, 'operation': 'add'},
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['result'] == 8

def test_calculate_divide_by_zero(client):
    response = client.post('/calculate',
                          json={'a': 5, 'b': 0, 'operation': 'divide'},
                          content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data

def test_calculate_missing_params(client):
    response = client.post('/calculate',
                          json={'a': 5},
                          content_type='application/json')
    assert response.status_code == 400