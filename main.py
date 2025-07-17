
from src.utils.send_email import send_email
# from src.utils.read_worksheet import read_worksheet
from src.messaging.delivery_message import delivery_message

report = delivery_message()

send_email(
    to='gabrielk1209@gmail.com',
    subject=report['subject'],
    body=report['body']
        
)
