def test_notes_page(client):
    response = client.get("/notes")
    assert response.status_code == 200

# def test_notes_page(client):
#     response = client.get('/notes/1')
#     assert response.status_code == 200

def test_notes_page_not_found(client):
    err_response = client.get('/notes/68')
    assert err_response.status_code == 404

def test_create_note(client):
    data = {
        "sender_id": 1,
        "text": "Oregon",
        "guide_id":1,
        "timestamp": '798'

    }
    response = client.post('/notes', json=data)
    assert response.status_code == 201

def test_get_note_by_guide(client):
    response = client.get('/notes/guide/1')
    assert response.status_code ==200
