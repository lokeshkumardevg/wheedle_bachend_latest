import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://devclientg:SCpLNaejWusV7mcR@cluster0.vyinynw.mongodb.net/wheedle_backend")
JWT_SECRET = os.getenv("JWT_SECRET", "wheedle_secret_key")

if not OPENAI_API_KEY:
    # raise ValueError("OPENAI_API_KEY not found")
    print("WARNING: OPENAI_API_KEY not found")

if not API_KEY_SECRET:
    # raise ValueError("API_KEY_SECRET not found")
    print("WARNING: API_KEY_SECRET not found")

client = None
if OPENAI_API_KEY:
    client = OpenAI(api_key=OPENAI_API_KEY)
