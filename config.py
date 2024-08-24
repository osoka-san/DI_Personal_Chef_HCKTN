from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_API_KEY = "sk-svcacct-7RKvYv2IOwtYu25Z4mYGN8FE1ujsti5jemKuCNa6FVz-6DDyRVhITWpSMKw6g3cMT3BlbkFJla3-v60CWHOwazE_3uWQ69E0CILKAxItZwwjz2Ntn92lZpZPV-5XRoQO-eCp2o4A"

    DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1000))
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
print("Config.py is being loaded")
