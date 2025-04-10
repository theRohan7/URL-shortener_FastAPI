import os 
from dotenv import load_dotenv

load_dotenv()

class  Settings:
    DATABASE_URL = os.getenv('DATABASE_URL')
    BASE_URL = os.getenv('BASE_URL')

settings = Settings() 