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

def test_update_guide(client):
    data = {
        'tagline': 'tag'
    }

    response = client.patch('/guides/1', json=data)
    assert response.status_code == 201

def test_guides_page(client):
    response = client.get("/guides")
    assert response.status_code == 200

def test_find_guide_by_username(client):
    response = client.get('/guides/username/guydunn42')  
    assert response.status_code == 200

def test_find_guide_by_email(client):
    response = client.get('/guides/email/guy.dunn@gmail.com')  
    assert response.status_code == 200

def test_find_guide_by_email_error(client):
    response = client.get('/guides/email/none')  
    assert response.status_code == 500

def test_find_guide_by_username_error(client):
    response = client.get('/guides/username/none')  
    assert response.status_code == 500

def test_find_guide_by_index(client):
    response = client.get('/guides/1')  
    assert response.status_code == 200


# def test_find_guide_by_index_error(client):
#     response = client.get('/guides/99')  
#     assert response.status_code == 404

def test_find_guides_by_place_id(client):
    response = client.get('/guides/placeId:2')
    assert response.status_code == 200

def test_find_guides_by_place_id_error(client):
    response = client.get('/guides/placeId:')
    assert response.status_code == 404

def test_find_activity_by_guide(client):
    res = client.get('/guides/guideId:1/activities')
    assert res.status_code == 200

def test_handle_guide_login(client):
    data = {
        'name': 'John Doe',
        'user_type': 'GUIDE',
        'username': 'test_username',
        'email': 'test@example.com',
        'password': 'test_password'
    }
    client.post('/guides/register', json=data)

    login_data = {
        'email': 'test@example.com',
        'password': 'test_password'
    }
    response = client.post('/guides/login', json=login_data)
    assert response.status_code == 200
    assert 'tokens' in response.json

def test_handle_user_login_invalid_credentials(client):
    login_data = {
        'email': 'nonexistent@example.com',
        'password': 'invalid_password'
    }
    response = client.post('/guides/login', json=login_data)
    assert response.status_code == 400

def test_protected_route_current_guide_missing_token(client):
    response = client.get('/guides/current')
    assert response.status_code == 401







