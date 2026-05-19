from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_root_returns_welcome_message():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_version_endpoint_returns_correct_data():
    response = client.get("/version")
    assert response.status_code == 200
    data = response.json()
    assert data["version"] == "1.0.0"
    assert "environment" in data


def test_version_and_health_match_environment():
    health = client.get("/health").json()
    version = client.get("/version").json()

    assert health["environment"] == version["environment"]
