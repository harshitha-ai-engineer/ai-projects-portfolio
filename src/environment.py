
"""
Enterprise AI Platform
Environment Configuration Module
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read application settings
APP_ENV = os.getenv("APP_ENV", "development")

DEBUG = os.getenv("DEBUG", "false").lower() == "true"

AI_PROVIDER = os.getenv("AI_PROVIDER", "openai")

API_KEY = os.getenv("API_KEY")


def get_environment_config():

    return {
        "app_env": APP_ENV,
        "debug": DEBUG,
        "ai_provider": AI_PROVIDER,
        "api_key_configured": bool(API_KEY)
    }
