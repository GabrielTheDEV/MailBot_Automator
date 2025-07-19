from src.utils.read_worksheet import read_worksheet
from src.templates.emails_template import email_template

def financial_message() -> dict:
    data = read_worksheet()

    columns = [
        'Data de emissão','Carga','Cliente','Origem',
        'Destino','Status','Valor Frete'
    ]
    if all(c in data.columns for c in columns):
        data = data[columns]

    table_html = data.to_html(index=False, border=1)

    message = {
        'subject':'RELATORIO FINANCEIRO DA SEMANA',
        'body': email_template('Segue o relatorio financeiro da semana', table_html)
        
    }
    return message