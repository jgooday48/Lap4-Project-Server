import json
    


def test_index_page(client):
    response = client.get("/")    
    assert response.status_code == 200     

# GET /places
def test_activities_page(client):
    response = client.get("/activities")
    assert response.status_code == 200

def test_activity_page(client):
    response = client.get('/activities/1')
    assert response.status_code == 200

def test_activity_page_not_found(client):
    err_response = client.get('/activities/68')
    assert err_response.status_code == 404


# def test_create_place(client):
#     data = {
#         "name": "Los Angeles",
#         "location": "California",
#         "description": "Largest city on the west coast of USA",
#         "tags": "#Hollywood"
#     }
#     response = client.post('/activities', json=data)
#     assert response.status_code == 201
#     created_data = json.loads(response.data)
#     assert "data" in created_data

def test_create_activity_error(client):
    data = {
        "location": "France"
    }
    response = client.post('/activities', json=data)
    assert response.status_code == 400

def test_update_activity(client):
    data = {
        "location": "America"
    }
    response = client.patch('/activities/1', json=data)
    assert response.status_code == 200
    updated_data = json.loads(response.data)
    assert "data" in updated_data

def test_delete_activity(client):
    response = client.delete('/activities/1')
    assert response.status_code == 204  
    assert response.data == b''  
