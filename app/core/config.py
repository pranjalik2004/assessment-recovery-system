import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

print("Loaded DB URL:", DATABASE_URL)  # 👈 add this for debugging
