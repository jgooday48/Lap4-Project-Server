

def test_chat_page(client):
    response = client.get("/chat")
    assert response.status_code == 200

# def test_activity_page(client):
#     response = client.get('/activities/1')
#     assert response.status_code == 200

# def test_chat_page_not_found(client):
#     err_response = client.get('/chat/68')
#     assert err_response.status_code == 404
