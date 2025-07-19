# Entregas
from src.utils.read_worksheet import read_worksheet
from src.templates.emails_template import email_template

def delivery_message() -> dict:
    data = read_worksheet()
    delivered = data[data['Status'] == 'Entregue']

    columns = [
        'Data de emissão','Carga','Cliente','Origem',
        'Destino','Motorista','Veículo','Previsão Entrega',
        'Entrega Realizada','Status','Valor Frete'
    ]
    if all(c in delivered.columns for c in columns):
        delivered = delivered[columns]

    table_html = delivered.to_html(index=False, border=1)

    message = {
        'subject':'RELATORIO DE ENTREGAS DA SEMANA',
        'body': email_template('Relatorio De Entregas Da Semana', table_html)
        
    }
    return message