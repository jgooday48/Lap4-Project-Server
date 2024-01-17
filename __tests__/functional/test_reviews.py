import json
import pytest
from datetime import datetime  
# GET /reviews
def test_reviews_page(client):
    response = client.get("/reviews")
    assert response.status_code == 200

def test_review_page(client):
    response = client.get('/reviews/1')
    assert response.status_code == 200

def test_review_page_not_found(client):
    err_response = client.get('/reviews/68')
    assert err_response.status_code == 404

@pytest.mark.skip(reason="need to fix")
def test_create_review(client):
    data = {
        "guide_id": 1,
        "tourist_id": 1,
        "rating": 5,
        "title": "review",
        "comment": "very nice",


    }
    response = client.post('/reviews', json=data)
    assert response.status_code == 201
    # created_data = json.loads(response.data)
    # assert "data" in created_data


def test_create_review_error(client):
    data = {
        "comment": "Poor"
    }
    response = client.post('/reviews', json=data)
    assert response.status_code == 400

# @pytest.mark.skip(reason="Test is skipped for a specific reason")
def test_update_review(client):
    data = {
        "comment": "America"
    }
    response = client.patch('/reviews/1', json=data)
    assert response.status_code == 200
    updated_data = json.loads(response.data)
    assert "data" in updated_data

# @pytest.mark.skip(reason="Test is skipped for a specific reason")
def test_update_review_error(client):
    data = {
        "comment": "America"
    }
    response = client.patch('/reviews/500', json=data)
    assert response.status_code == 404


def test_delete_review(client):
    response = client.delete('/reviews/1')
    assert response.status_code == 204  
    assert response.data == b'' 

# @pytest.mark.skip(reason="Test is skipped for a specific reason")
def test_delete_review_error(client):
    response = client.delete('/reviews/100')
    assert response.status_code == 404 

