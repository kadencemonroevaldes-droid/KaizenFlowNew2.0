from pathlib import Path
import sys

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.main import app  # noqa: E402


client = TestClient(app)


def test_dashboard_renders():
    response = client.get("/")
    assert response.status_code == 200
    assert "Kaizen Flow" in response.text
    assert "Dashboard" in response.text


def test_tracker_renders():
    response = client.get("/tracker")
    assert response.status_code == 200
    content = response.text.lower()
    assert "kaizen flow" in content
    assert "add new idea" in content or "add a new initiative" in content


def test_culture_renders():
    response = client.get("/culture")
    assert response.status_code == 200
    content = response.text.lower()
    assert "culture lens" in content
    assert "reflect" in content or "reflection" in content
