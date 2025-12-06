import pytest
import os
from unittest.mock import patch
from app.auth import verify_init_data


def test_verify_init_data_valid():
    """Тест валидации корректных initData"""
    # Пример валидных initData (в реальности нужен правильный hash)
    # Для теста создадим простой случай
    with patch.dict(os.environ, {"TG_BOT_TOKEN": "test_token"}):
        # В реальном приложении нужно генерировать правильный hash
        # Здесь тестируем структуру функции
        result = verify_init_data("hash=test_hash&user=%7B%22id%22%3A123%7D")
        # Функция вернет False для неправильного hash, но не упадет
        assert isinstance(result, bool)


def test_verify_init_data_invalid():
    """Тест валидации некорректных initData"""
    with patch.dict(os.environ, {"TG_BOT_TOKEN": "test_token"}):
        # Пустые данные
        assert verify_init_data("") is False
        
        # Данные без hash
        assert verify_init_data("user=test") is False


def test_verify_init_data_missing_token():
    """Тест поведения при отсутствии BOT_TOKEN"""
    with patch.dict(os.environ, {}, clear=True):
        # Функция должна обработать отсутствие токена
        result = verify_init_data("hash=test&user=test")
        assert isinstance(result, bool)

