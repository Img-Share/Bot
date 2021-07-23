import pytest
from web import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_pet_response(client):
    response = client.get('/pet/non_existent.fffffff')
    assert response.status_code == 404

def test_index(client):
    assert client.get('/').status_code == 200
