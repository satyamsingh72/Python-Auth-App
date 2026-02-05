def test_login_success(client):
    # Register a user first
    client.post("/register", json={"username": "alice", "password": "mypassword"})

    response = client.post(
        "/login",
        json={"username": "alice", "password": "mypassword"}
    )

    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert isinstance(data["token"], str)


def test_login_invalid_username(client):
    response = client.post(
        "/login",
        json={"username": "wronguser", "password": "anything"}
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid Credentials"


def test_login_invalid_password(client):
    # Register valid user
    client.post("/register", json={"username": "bob", "password": "password123"})

    response = client.post(
        "/login",
        json={"username": "bob", "password": "wrongpass"}
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid Credentials"
