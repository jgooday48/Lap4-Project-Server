import json

def test_message_page(client):
    response = client.get("/message")
    assert response.status_code == 200

def test_message_page_indv(client):
    response = client.get('/message/1')
    assert response.status_code == 200


def test_message_page_ind(client):
    response = client.get('/message/100')
    assert len(response.json) == 0

def test_post_message(client):
    data = {
        "chat_id":1,
        "sender_id": 1,
        "text": 'a text'
    }
    response = client.post('/message', json=data)
    assert response.status_code == 200

# def test_post_message_err(client):
#     data = {
#         "chat_id":1,
#         "sender_id": 1
#     }
#     response = client.post('/message', json=data)
#     assert response.status_code == 400
