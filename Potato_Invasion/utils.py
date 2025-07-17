import sys
import os

def resource_path(relative_path):
    """Возвращает путь к ресурсу, работает и в .exe и в .py"""
    try:
        base_path = sys._MEIPASS  # путь для PyInstaller
    except Exception:
        base_path = os.path.abspath(".")  # обычный путь при запуске .py
    return os.path.join(base_path, relative_path)
