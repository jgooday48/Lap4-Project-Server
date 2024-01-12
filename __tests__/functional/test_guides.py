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

def test_find_guide_by_username(client):
    response = client.get('/guides/username/guydunn42')  
    assert response.status_code == 200

def test_find_guide_by_index(client):
    response = client.get('/guides/1')  
    assert response.status_code == 200


def test_find_guide_by_index_error(client):
    response = client.get('/guides/99')  
    assert response.status_code == 404

def test_find_guides_by_place_id(client):
    response = client.get('/guides/placeId:2')
    assert response.status_code == 200

def test_find_guides_by_place_id_error(client):
    response = client.get('/guides/placeId:')
    assert response.status_code == 404

def test_find_activ_by_guide(client):
    res = client.get('/guides/username:guydunn42/activities')
    assert res.status_code == 200

