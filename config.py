from dotenv import load_dotenv
import os

# Загружаем переменные окружения из файла .env, который находится в папке save.env
load_dotenv(dotenv_path=os.path.join("save.env", ".env"))

class Config:
    # Получаем API-ключ из переменной окружения
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Загружаем ключ API

    # Получаем другие параметры с дефолтными значениями
    DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1000))
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))

print("Config.py is being loaded")


