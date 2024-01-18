import json

def test_chat_page(client):
    response = client.get("/chat")
    assert response.status_code == 200

# def test_post_chat(client):
#     data = {
#         "sender": 1,
#         "receiver": 1
#     }

#     response = client.post('/chat', json=data)
#     assert response == 200


def test_find_sender(client):
    response = client.get('/chat/tourist/1')
    assert response == 200

def test_find_owner(client):
    response = client.get('/chat/guide/1')
    assert response == 200
