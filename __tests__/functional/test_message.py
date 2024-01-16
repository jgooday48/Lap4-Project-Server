import json

def test_message_page(client):
    response = client.get("/message")
    assert response.status_code == 200
