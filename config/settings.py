import os
from dotenv import load_dotenv



load_dotenv()
MONGODB_URL=os.getenv("MONGODB_URL")
MONGODB_DB = os.getenv("MANGODB_DB","FastAPI-DB")
