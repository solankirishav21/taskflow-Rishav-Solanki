def test_create_task(test_client):
    test_client.post("/auth/register", json={
        "name": "Test User",
        "email": "test@example.com",
        "password": "password123"
    })

    login = test_client.post("/auth/login", json={
        "email": "test@example.com",
        "password": "password123"
    })

    assert login.status_code == 200
    token = login.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}

    project = test_client.post("/projects", json={
        "name": "Test Project"
    }, headers=headers)

    project_id = project.json()["id"]

    response = test_client.post(
        f"/projects/{project_id}/tasks",
        json={"title": "Test Task"},
        headers=headers
    )

    assert response.status_code == 200