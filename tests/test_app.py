from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from merendapp_api.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_create_message(client):
    response = client.post(
        '/messages/',
        json={
            'name': 'Teste',
            'email': 'user@example.com',
            'phone': '11111111111',
            'company': 'Teste',
            'company_type': 'Escola',
            'message': 'test message',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'name': 'Teste',
        'email': 'user@example.com',
        'phone': '11111111111',
        'company': 'Teste',
        'company_type': 'Escola',
        'message': 'test message',
    }
