import pytest
from unittest.mock import patch
from conftest import client


def test_create_session_invalid_initdata(client):
    """Тест создания сессии с невалидными initData"""
    with patch("app.auth.verify_init_data", return_value=False):
        response = client.post("/api/session", json={"initData": "invalid_data"})
        assert response.status_code == 401
        assert "invalid initData" in response.json()["detail"]


def test_create_session_valid_initdata(client):
    """Тест создания сессии с валидными initData"""
    with patch("app.auth.verify_init_data", return_value=True):
        response = client.post("/api/session", json={"initData": "valid_data"})
        assert response.status_code == 200
        assert response.json() == {"ok": True}


def test_create_session_missing_initdata(client):
    """Тест создания сессии без initData"""
    response = client.post("/api/session", json={})
    assert response.status_code == 422  # Validation error

