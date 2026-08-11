from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_profissionais_sem_token():
    response = client.get("/profissional")

    assert response.status_code == 401