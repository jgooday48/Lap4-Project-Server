import json
import pytest


def test_handle_guide_register(client): 
    data = {
        'username': 'test_username',
        'email': 'test@example.com',
        'user_type': 'Guide',
        'name': 'Dunn Guide',
        'filters': ['filter1', 'filter2'],
        'password': 'test_password'
    }

    response = client.post('/guides/register', json=data)
    assert response.status_code == 201

def test_guides_page(client):
    response = client.get("/guides")
    assert response.status_code == 200
