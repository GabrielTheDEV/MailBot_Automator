import smtplib #biblioteca para envio de emails através do protocolo SMTP

from src.config.config import EMAIL, PASS, SMTP_SERVER, SMTP_PORT

def email_sender(to:str ,subject:str, body ):


    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASS)
        # server.send_message(msg)


