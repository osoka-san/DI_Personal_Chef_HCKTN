from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_API_KEY = "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"

    DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1000))
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
print("Config.py is being loaded")
