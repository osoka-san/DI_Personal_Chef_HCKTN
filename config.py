from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    OPENAI_API_KEY = "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"

    DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1000))
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
print("Config.py is being loaded")
