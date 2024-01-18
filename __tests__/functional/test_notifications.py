def test_notification_page(client):
    response = client.get("/notifications")
    assert response.status_code == 200

# def test_notes_page(client):
#     response = client.get('/notes/1')
#     assert response.status_code == 200

def test_notes_page_not_found(client):
    err_response = client.get('/notifications/68')
    assert err_response.status_code == 404

def test_create_notification(client):
    data = {
        "sender": 1,
        "receiver": 1

    }
    response = client.post('/notifications', json=data)
    assert response.status_code == 201

# def test_get_note_by_guide(client):
#     response = client.get('/notes/guide/1')
#     assert response.status_code ==200
