#!/usr/bin/env python
"""
Скрипт для запуска всех тестов проекта
"""
import subprocess
import sys
from pathlib import Path

def run_tests():
    """Запускает все тесты проекта"""
    project_root = Path(__file__).parent
    
    print("=" * 60)
    print("Запуск тестов Content Planner")
    print("=" * 60)
    
    # Тесты API
    print("\n[1/2] Запуск тестов API (planner/tests/)...")
    print("-" * 60)
    result_api = subprocess.run(
        [sys.executable, "-m", "pytest", "planner/tests/", "-v"],
        cwd=project_root
    )
    
    # Тесты бота
    print("\n[2/2] Запуск тестов бота (bot/tests/)...")
    print("-" * 60)
    result_bot = subprocess.run(
        [sys.executable, "-m", "pytest", "bot/tests/", "-v"],
        cwd=project_root
    )
    
    # Итоги
    print("\n" + "=" * 60)
    print("Итоги:")
    print(f"  API тесты: {'✓ PASSED' if result_api.returncode == 0 else '✗ FAILED'}")
    print(f"  Бот тесты: {'✓ PASSED' if result_bot.returncode == 0 else '✗ FAILED'}")
    print("=" * 60)
    
    return result_api.returncode == 0 and result_bot.returncode == 0

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)

