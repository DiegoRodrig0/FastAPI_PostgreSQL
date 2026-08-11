from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_paciente_sem_token():
    response = client.get("/paciente")

    assert response.status_code == 401