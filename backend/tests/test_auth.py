def test_register(test_client):
    response = test_client.post("/auth/register", json={
        "name": "Test User",
        "email": "test123@example.com",
        "password": "password123"
    })

    assert response.status_code in [200, 400]  # handle duplicate


def test_login(test_client):
    response = test_client.post("/auth/login", json={
        "email": "test123@example.com",
        "password": "password123"
    })

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data