def test_register_success(client):
    response = client.post(
        "/register",
        json={"username": "john", "password": "secret123"}
    )

    assert response.status_code == 200
    assert response.json() == {"message": "User Registered"}