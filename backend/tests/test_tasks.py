def test_create_task(test_client):
    login = test_client.post("/auth/login", json={
        "email": "test@example.com",
        "password": "password123"
    })

    token = login.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    projects = test_client.get("/projects", headers=headers)
    project_id = projects.json()[0]["id"]

    response = test_client.post(
        f"/projects/{project_id}/tasks",
        json={"title": "Test Task"},
        headers=headers
    )

    assert response.status_code == 200