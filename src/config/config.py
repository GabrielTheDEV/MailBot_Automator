import os
from dotenv import load_dotenv

load_dotenv()

EMAIL : str = os.getenv("EMAIL")
PASS : str = str(os.getenv("EMAIL_PASSWORD"))

SERVER_SMTP : str = 'smtp.gmail.com' # smtp o protocolo utilizado para envio de emails
PORT : int = 465

SERVER_IMAP : str = 'imap.gmail.com'