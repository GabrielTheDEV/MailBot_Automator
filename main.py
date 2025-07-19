from src.utils.send_email import send_email
from src.messaging.delivery_message import delivery_message
from src.messaging.delay_message import delay_message
from src.messaging.financial_message import financial_message
from src.utils.read_emails import read_emails

delivery_report = delivery_message()
financial_report = financial_message()
delay_report = delay_message()

send_email(
    to=['gabrielk1209@gmail.com'],
    subject=delivery_report['subject'],
    body=delivery_report['body']
)
send_email(
    to=['gabrielk1209@gmail.com'],
    subject=delay_report['subject'],
    body=delay_report['body']
        
)
send_email(
    to=['gabrielk1209@gmail.com'],
    subject=financial_report['subject'],
    body=financial_report['body']
        
)

read_emails()
