import os
import pytest
from main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
