from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_profissionais_sem_token():
    response = client.get("/profissional")

    assert response.status_code == 401

def test_profissionais_com_token():

    login = client.post(
        "/auth/login",
        data={
            "username": "test@email.com.br",
            "password": "test12345"
        }
    )

    assert login.status_code == 200

    token = login.json()["access_token"]

    response = client.get(
        "/profissional",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200