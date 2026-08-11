from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_equipe_sem_token():
    response = client.get("/equipes")

    assert response.status_code == 401