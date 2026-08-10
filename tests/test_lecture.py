from http import HTTPStatus
from fastapi.testclient import TestClient

from fastzero.lecture import app

def test_lecture():
    test_client = TestClient(app)

    response = test_client.get('/lecture')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Ola Mundo</h1>' in response.text