import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from src.config.config import EMAIL, PASS, SERVER_SMTP, PORT

def send_email(to: list, subject: str, body: str):
    msg = MIMEMultipart("alternative")

    if isinstance(to , list ): # <-- converte lista de emails em strings
        msg["To"] =", ".join(to)
    else :
        msg["To"] = to

    msg["From"] = EMAIL
    msg["Subject"] = subject

    body_msg = MIMEText(body, "html")
    msg.attach(body_msg)

    try:
        with smtplib.SMTP_SSL(SERVER_SMTP, PORT) as server:
            server.login(EMAIL, PASS)
            server.send_message(msg)
        print("[ SUCESSO ] E-mail enviado com sucesso!")
    except Exception as err:
        print("[ ERROR ] Erro ao enviar e-mail:", err)

