import os
from dotenv import load_dotenv

load_dotenv()


def get_credentials():
    """
    Extracts gmail credentials from env
    """
    return os.getenv("EMAIL"), os.getenv("PASSWORD")
