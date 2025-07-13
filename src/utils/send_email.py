import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from src.config.config import EMAIL, PASS, SERVER_SMTP, PORT

def send_email(to: str, subject: str, body: str):
    msg = MIMEMultipart("alternative")
    msg["From"] = EMAIL
    msg["To"] = to
    msg["Subject"] = subject

    body_msg = MIMEText(body, "html")
    msg.attach(body_msg)

    try:
        with smtplib.SMTP_SSL(SERVER_SMTP, PORT) as server:
            server.login(EMAIL, PASS)
            server.send_message(msg)
        print("[ DONE ] E-mail enviado com sucesso!")
    except Exception as err:
        print("[ ERROR ] Erro ao enviar e-mail:", err)

# Exemplo de uso:
