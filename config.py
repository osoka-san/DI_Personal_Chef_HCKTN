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
