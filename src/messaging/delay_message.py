from src.utils.read_worksheet import read_worksheet
def delay_message():
    data = read_worksheet()
    delayed = data[data['Status'] == 'Atrasada' ]

    columns = [
        'Data de emissão','Carga','Cliente','Origem',
        'Destino','Motorista','Veículo','Previsão Entrega',
        'Entrega Realizada','Status','Valor Frete'
    ]

    if all(c in delayed.columns for c in columns):
        delayed = delayed[columns]

    table_html = delayed.to_html(index=False, border=1)

    message = {
        'subject':'RELATORIO FINANCEIRO DA SEMANA',
        'body': f'<h1>Segue o relatorio financeiro da semana</h1>{table_html}'
        
    }
    return message