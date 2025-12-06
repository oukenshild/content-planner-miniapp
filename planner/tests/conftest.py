import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Фикстура для тестового клиента FastAPI"""
    return TestClient(app)

