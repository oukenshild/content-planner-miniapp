import pytest
from datetime import date
from conftest import client


def test_calendar_range(client):
    """Тест получения постов за период"""
    start_date = "2024-01-01"
    end_date = "2024-01-31"
    response = client.get(f"/api/calendar/range?start={start_date}&end={end_date}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_calendar_range_missing_params(client):
    """Тест получения постов без параметров"""
    response = client.get("/api/calendar/range")
    assert response.status_code == 422  # Validation error


def test_calendar_range_invalid_date(client):
    """Тест получения постов с невалидной датой"""
    response = client.get("/api/calendar/range?start=invalid&end=2024-01-31")
    assert response.status_code == 422  # Validation error


def test_calendar_range_reverse_dates(client):
    """Тест получения постов когда start > end"""
    start_date = "2024-01-31"
    end_date = "2024-01-01"
    response = client.get(f"/api/calendar/range?start={start_date}&end={end_date}")
    # Текущая реализация не проверяет порядок дат
    assert response.status_code == 200

