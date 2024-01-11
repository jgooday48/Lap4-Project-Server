import json

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
