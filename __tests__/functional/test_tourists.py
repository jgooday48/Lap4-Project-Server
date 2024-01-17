import json
from flask_jwt_extended import create_access_token
from application.tourists.model import Tourist
def test_handle_tourist_register(client): 
    data = {
        'name': 'John Doe',
        'user_type': 'TOURIST',
        'username': 'test_username',
        'email': 'test@example.com',
        'password': 'test_password'
    }

    response = client.post('/tourists/register', json=data)
    assert response.status_code == 201

def test_find_tourist_by_username(client):
    response = client.get('/tourists/username/johnsmith456')  
    assert response.status_code == 200

def test_find_tourist_by_email(client):
    response = client.get('/tourists/email/john.smith@gmail.com')  
    assert response.status_code == 200

def test_find_tourist_by_email_error(client):
    response = client.get('/tourists/email/john.smith@gmail')  
    assert response.status_code == 500
    assert response.json == {"message": "User not found"}

def test_find_tourist_by_username_error(client):
    response = client.get('/tourists/username/johnsmith45')
    assert response.status_code == 500
    assert response.json == {"message": "User not found"}

def test_tourist_db_no_auth(client):
    response = client.get('http://localhost:5000/tourists/current')
    assert response.json == {"msg": "Missing Authorization Header"}


def test_find_tourist_by_id(client):
    response = client.get('/tourist/1')
    assert response.status_code == 200



def test_handle_tourist_register_existing_username(client):

    data = {
        'name': 'John Doe',
        'user_type': 'TOURIST',
        'username': 'existing_username',
        'email': 'test@example.com',
        'password': 'test_password'
    }
    response = client.post('/tourists/register', json=data)
    assert response.status_code == 201
    response_existing_username = client.post('/tourists/register', json=data)
    assert response_existing_username.status_code == 403

def test_handle_user_login(client):

    data = {
        'name': 'John Doe',
        'user_type': 'TOURIST',
        'username': 'test_username',
        'email': 'test@example.com',
        'password': 'test_password'
    }
    client.post('/tourists/register', json=data)

    login_data = {
        'email': 'test@example.com',
        'password': 'test_password'
    }
    response = client.post('/tourists/login', json=login_data)
    assert response.status_code == 200
    assert 'tokens' in response.json

def test_handle_user_login_invalid_credentials(client):
    login_data = {
        'email': 'nonexistent@example.com',
        'password': 'invalid_password'
    }
    response = client.post('/tourists/login', json=login_data)
    assert response.status_code == 400



def test_protected_route_current_tourist(client):
    data = {
        'name': 'John Doe',
        'user_type': 'TOURIST',
        'username': 'protected_route_user',
        'email': 'protected_route@example.com',
        'password': 'test_password'
    }
    client.post('/tourists/register', json=data)

    login_data = {
        'email': 'protected_route@example.com',
        'password': 'test_password'
    }
    login_response = client.post('/tourists/login', json=login_data)
    assert login_response.status_code == 200
    access_token = login_response.json['tokens']['access']


    headers = {'Authorization': f'Bearer {access_token}'}
    response = client.get('/tourists/current', headers=headers)
    assert response.status_code == 200
    assert 'user_details' in response.json

def test_protected_route_current_tourist_missing_token(client):
    response = client.get('/tourists/current')
    assert response.status_code == 401



def test_find_guides_by_tourist_not_found(client):

    response = client.get('/tourists/999/guides')
    assert response.status_code == 404

def test_remove_tourist_guide_pair_invalid_ids(client):

    response = client.delete('/tourists/guides/')
    assert response.status_code == 404




