import json
import pytest

# GET /plans
def test_plans_page(client):
    response = client.get("/plans")
    assert response.status_code == 200

def test_plan_page(client):
    response = client.get('/plans/1')
    assert response.status_code == 200

def test_plan_page_not_found(client):
    err_response = client.get('/plans/68')
    assert err_response.status_code == 404


def test_create_plan(client):
    data = {
        "tourist_id":1,
        "guide_id":1,
        "date_from": "2024-01-12 10:50:29.918223",
        "date_to": "2024-01-12 10:50:29.918223",
        "activity_id": 1,
        "status":"PLANNED"
    }
    response = client.post('/plans', json=data)
    assert response.status_code == 201
    created_data = json.loads(response.data)
    assert "data" in created_data

def test_create_plan_error(client):
    data = {
        "activity_id": 1
    }
    response = client.post('/plans', json=data)
    assert response.status_code == 400

def test_update_plan(client):
    data = {
        "timestamp": 10
    }
    response = client.patch('/plans/1', json=data)
    assert response.status_code == 200
    updated_data = json.loads(response.data)
    assert "data" in updated_data


def test_update_plan_error(client):
    data = {
        "timestamp": 10
    }
    response = client.patch('/plans/500', json=data)
    assert response.status_code == 404

def test_delete_plan(client):
    response = client.delete('/plans/1')
    assert response.status_code == 204  
    assert response.data == b''  

def test_delete_plan_error(client):
    response = client.delete('/plans/70')
    assert response.status_code == 404  

