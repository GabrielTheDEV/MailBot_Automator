from src.utils.read_worksheet import read_worksheet
from src.templates.emails_template import email_template

def financial_message() -> dict:
    data = read_worksheet()

    columns = [
        'Data de emissão','Carga','Cliente','Origem',
        'Destino','Status','Valor Frete, Status de Pagamento'
    ]
    #Resumo Financeiro:
        #Total faturado no mês: R$ 42.500,00
        #Pagamentos pendentes: R$ 3.200,00
        #Pagamentos recebidos: R$ 39.300,00

    if all(c in data.columns for c in columns):
        data = data[columns]

    table_html = data.to_html(index=False, border=1)

    message = {
        'subject':'RELATORIO FINANCEIRO DA SEMANA',
        'body': email_template('Segue o relatorio financeiro da semana', table_html, '')
    }
    return message