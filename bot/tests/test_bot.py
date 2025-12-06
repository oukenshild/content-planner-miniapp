import pytest
import sys
import importlib
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch
from aiogram import types

# Добавляем путь к модулю bot
sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.mark.asyncio
async def test_start_command():
    """Тест обработки команды /start"""
    with patch.dict("os.environ", {"TG_WEBAPP_URL": "https://example.com", "TG_BOT_TOKEN": "test_token"}):
        import bot.bot as bot_module
        importlib.reload(bot_module)
        
        # Создаем мок сообщения
        message = MagicMock(spec=types.Message)
        message.answer = AsyncMock()
        
        # Вызываем обработчик
        await bot_module.start(message)
        
        # Проверяем, что был вызван answer
        assert message.answer.called
        
        # Проверяем аргументы вызова
        call_args = message.answer.call_args
        assert call_args is not None
        
        # Проверяем текст сообщения
        assert "Открой планировщик:" in call_args[0][0]
        
        # Проверяем наличие reply_markup
        assert call_args[1]["reply_markup"] is not None
        reply_markup = call_args[1]["reply_markup"]
        
        # Проверяем, что это ReplyKeyboardMarkup
        assert isinstance(reply_markup, types.ReplyKeyboardMarkup)
        
        # Проверяем наличие кнопки
        assert len(reply_markup.keyboard) > 0
        button = reply_markup.keyboard[0][0]
        assert button.text == "Open planner"
        assert button.web_app is not None
        assert isinstance(button.web_app, types.WebAppInfo)


@pytest.mark.asyncio
async def test_start_command_webapp_url():
    """Тест проверки наличия WebApp URL в кнопке"""
    with patch.dict("os.environ", {"TG_WEBAPP_URL": "https://example.com", "TG_BOT_TOKEN": "test_token"}):
        import bot.bot as bot_module
        importlib.reload(bot_module)
        
        message = MagicMock(spec=types.Message)
        message.answer = AsyncMock()
        
        await bot_module.start(message)
        
        call_args = message.answer.call_args
        reply_markup = call_args[1]["reply_markup"]
        button = reply_markup.keyboard[0][0]
        
        assert button.web_app.url == "https://example.com"

