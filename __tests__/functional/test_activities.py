import json
import pytest

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

@pytest.mark.skip(reason="Test is skipped for a specific reason")
def test_create_activity(client):
    data = {
        "name": "sailing",
        "location": "Oregon",
        "specialisation": "OUTDOOR_ACTIVITIES",
        "place_id": 1,
        "description": "jkl",
        "zip_code": "90210"
    }
    response = client.post('/activities', json=data)
    assert response.status_code == 201
    # created_data = json.loads(response.data)
    # assert "data" in created_data

# @pytest.mark.skip(reason="Test is skipped for a specific reason")
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

# @pytest.mark.skip(reason="Test is skipped for a specific reason")
def test_update_activity_error(client):
    data = {
        "location": "America"
    }
    response = client.patch('/activities/500', json=data)
    assert response.status_code == 404

# # @pytest.mark.skip(reason="Test is skipped for a specific reason")
# def test_delete_activity(client):
#     response = client.delete('/activities/1')
#     assert response.status_code == 204  
#     # assert response.data == b'' 

# # @pytest.mark.skip(reason="Test is skipped for a specific reason")
# def test_delete_activity_error(client):
#     response = client.delete('/activities/100')
#     assert response.status_code == 404  

