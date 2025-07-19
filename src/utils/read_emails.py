#Leitura dos emails
#Utilizei a biblioteca imaplib para leitura dos emails
import imaplib
from src.utils.save_email import save_email
from src.config.config import EMAIL, PASS, SERVER_IMAP

def read_emails():
    # Connection
    email = imaplib.IMAP4_SSL(SERVER_IMAP)
    email.login(EMAIL,PASS)
    email.select('inbox')

    status, msg = email.search(None, '(UNSEEN)')
    emails_ids = msg[0].split()

    for id in emails_ids:
        status, datas = email.fetch(id, '(RFC822)') # ( EFC822) é o formato padrão de mensagem de email (txt + cabeçalho)
        for response_part in datas:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])
                email_id = message.get("From")
                body = ""
                if message.is_multipart():
                    for part in message.walk():
                        if part.get_content_type() == "text/plain":
                           body+= part.get_payload(decode=True).decode()
                else:
                           body+= message.get_payload(decode=True).decode()
                if "Cadastre meu email" in body.lower():
                    print('Email salvo')
                    save_email(email_id)
    email.logout()