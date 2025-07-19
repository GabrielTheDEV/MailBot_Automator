from src.utils.read_worksheet import read_worksheet

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
        'body': f'<h1>Segue o relatorio financeiro da semana</h1>{table_html}'
        
    }
    return message