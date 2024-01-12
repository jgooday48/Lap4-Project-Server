import json
import pytest


def test_handle_guide_register(client): 
    data = {
        'username': 'test_username',
        'email': 'test@example.com',
        'user_type': 'GUIDE',
        'name': 'Dunn Guide',
        'filters': ['HISTORICAL', 'MUSIC'],
        'password': 'test_password',
        'availible_from': '2024-01-12 10:50:29.918223',
        'availible_to': '2024-01-12 10:50:29.918223'

    }

    response = client.post('/guides/register', json=data)
    assert response.status_code == 201

def test_guides_page(client):
    response = client.get("/guides")
    assert response.status_code == 200

def test_guide_exists(client):
    pass
