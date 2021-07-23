import pytest
from web import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_pet_response(client):
    response = client.get('/pets/non_existent.fffffff')
    assert response.status_code == 404

def test_index(client):
    imghub_welcome_text = """
<h1>Welcome to Img.Hub</h1>
<p>Img.Hub is an experimental web UI for Img.Share. It allows you to browse and share images from Img.Share.</p>
<p>Expect bugs.</p>
"""
    assert client.get('/').status_code == 200
    assert imghub_welcome_text in client.get('/').data.decode('utf-8')
    