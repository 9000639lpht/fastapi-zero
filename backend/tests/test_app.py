from http import HTTPStatus

from fastapi.testclient import TestClient

from fastzero.app import app


def test_hello_world():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'msg': 'Ola mundo!'}

def test_create_user():
    client = TestClient(app)

    response = client.post('/users/', json={
        'username': 'alice',
        'email': 'alice@example.com',
        'password': 'secret'
    })

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        "username": "alice",
        "email": "alice@example.com",
        "id": 1,
    } 