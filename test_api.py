import pytest
from api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_user(client):
    response = client.post('/users', json={'id': 1, "name": "Yoe"})
    
    assert response.status_code == 201
    assert response.json == {'id': 1, "name": "Yoe"}

def test_user_client(client):
    client.post('/users', json={'id': 2, "name": "Duni"})