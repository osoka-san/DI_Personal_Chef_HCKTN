from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1000))
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
print("Config.py is being loaded")
