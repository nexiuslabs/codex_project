from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_leads_default_pagination() -> None:
    response = client.get("/leads")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 10
    assert data[0]["id"] == 1


def test_read_leads_with_pagination() -> None:
    response = client.get("/leads", params={"page": 2, "size": 5})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5
    assert data[0]["id"] == 6
