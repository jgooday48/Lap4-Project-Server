import json
  

# GET /places
def test_places_page(client):
    response = client.get("/places")
    assert response.status_code == 200

def test_place_page(client):
    response = client.get('/places/1')
    assert response.status_code == 200

def test_place_page_not_found(client):
    err_response = client.get('/places/68')
    assert err_response.status_code == 404


def test_create_place(client):
    data = {
        "name": "Los Angeles",
        "location": "California",
        "description": "Largest city on the west coast of USA",
        "tags": ["#Hollywood"],
        "images": ["hkh"]
    }
    response = client.post('/places', json=data)
    assert response.status_code == 201
    created_data = json.loads(response.data)
    assert "data" in created_data
    assert response.json =={ 'data': {
        "place_id": 8,
        "name": "Los Angeles",
        "location": "California",
        "description": "Largest city on the west coast of USA",
        "tags": ["#Hollywood"],
        "images": ["hkh"]
    }}

def test_create_place_error(client):
    data = {
        "location": "France"
    }
    response = client.post('/places', json=data)
    assert response.status_code == 400

def test_update_place(client):
    data = {
        "location": "America"
    }
    response = client.patch('/places/1', json=data)
    assert response.status_code == 200
    updated_data = json.loads(response.data)
    assert "data" in updated_data

def test_update_place_error(client):
    data = {
        "location": "America"
    }
    response = client.patch('/places/500', json=data)
    assert response.status_code == 404

