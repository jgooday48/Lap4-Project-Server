import json
import pytest


def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200

def test_activities_page(client):
    response = client.get("/activities")
    assert response.status_code == 200

def test_activity_page(client):
    response = client.get('/activities/1')
    assert response.status_code == 200

def test_activity_page_not_found(client):
    err_response = client.get('/activities/68')
    assert err_response.status_code == 404


def test_create_activity(client):
    data = {
        "name": "sailing",
        "location": "Oregon",
        "filters": ["OUTDOOR_ACTIVITIES"],
        "place_id": 1,
        "description": "jkl",
        "zip_code": "90210",
        "images": ['sfkgfe']
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



def test_find_guides_by_activity(client):
    response = client.get('/activities:1/guides') 
    assert response.status_code == 200

def test_find_guides_by_activity_error(client):
    response = client.get('/activities:100/guides') 
    assert response.status_code == 404
