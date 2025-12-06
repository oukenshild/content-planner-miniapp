import pytest
from conftest import client


def test_add_comment(client):
    """Тест добавления комментария"""
    comment_data = {
        "post_id": 1,
        "text": "Test comment"
    }
    response = client.post("/api/comments", json=comment_data)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["post_id"] == comment_data["post_id"]
    assert data["text"] == comment_data["text"]
    assert "created_at" in data


def test_add_comment_missing_fields(client):
    """Тест добавления комментария без обязательных полей"""
    response = client.post("/api/comments", json={})
    assert response.status_code == 422  # Validation error


def test_add_comment_empty_text(client):
    """Тест добавления комментария с пустым текстом"""
    comment_data = {
        "post_id": 1,
        "text": ""
    }
    response = client.post("/api/comments", json=comment_data)
    # Текущая реализация принимает пустой текст
    assert response.status_code == 200

