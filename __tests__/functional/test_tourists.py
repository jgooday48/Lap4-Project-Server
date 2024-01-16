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

def test_find_tourist_by_username_error(client):
    response_not_found = client.get('/tourists/username/johnsmith45')
    assert response_not_found.status_code == 500
    assert response_not_found.json == {"message": "User not found"}

def test_tourist_db_no_auth(client):
    response_not_found = client.get('http://localhost:5000/tourists/current')
    assert response_not_found.json == {"msg": "Missing Authorization Header"}


def test_find_tourist_by_id(client):
    response = client.get('/tourist/1')
    assert response.status_code == 200


# def test_delete_tourist_guide_pair(client):
#     response = client.delete('/tourists/guides/1/1')
#     assert response == 204
