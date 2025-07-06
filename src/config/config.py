import os
from dotenv import load_dotenv # biblioteca que acessa váriaveis de ambientes 

load_dotenv()

EMAIL: str = os.getenv("EMAIL")
PASS: str = str(os.getenv("PASSWORD"))
SMTP_SERVER: str = os.getenv("SMTP_SERVER")
SMTP_PORT: int = int( os.getenv("SMTP_PORT"))