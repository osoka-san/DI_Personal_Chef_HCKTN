from dotenv import load_dotenv
import os

# Загружаем переменные окружения из файла .env
load_dotenv()

class Config:
    # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_API_KEY = "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"

    # Получаем другие параметры с дефолтными значениями
    DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1000))
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))

print("Config.py is being loaded")

