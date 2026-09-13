import os
from dotenv import load_dotenv

load_dotenv()

# Gemini API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

#Gemini model
GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)

#App configuration
APP_NAME = os.getenv(
    "APP_NANE",
    "Gemini AI_Agent"
)
APP_VERSION = os.getenv(
    "APP_VERSION",
    "0.1"
)

# Validate required configuration
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is not configured.",
        "Add it to your .env file"
    )