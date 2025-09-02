import pytest
from app import app  # assumes your app is saved as `app.py`

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello world from CI/CD" in response.data
