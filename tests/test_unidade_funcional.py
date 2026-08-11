from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_unidade_funcional_sem_token():
    response = client.get("/unidades")

    assert response.status_code == 401