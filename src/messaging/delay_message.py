from src.utils.read_worksheet import read_worksheet
from src.templates.emails_template import email_template
def delay_message():
    data = read_worksheet()
    delayed = data[data['Status'] == 'Atrasada' ]

    columns = [
        'Data de emissão','Carga','Cliente','Origem',
        'Destino','Motorista','Veículo','Previsão Entrega',
        'Entrega Realizada','Status','Valor Frete'
    ]
    delayed_orders : int = len(delayed)
    delayed_percentage : int = 0
    if len(data) > 0 :
        delayed_percentage = (delayed_orders / len(data)) * 100
    else:
        delayed_orders = 0

    if all(c in delayed.columns for c in columns):
        delayed = delayed[columns]

    table_html = delayed.to_html(index=False, border=1)

    message = {
        'subject':'RELATORIO DE CARGAS ATRASADOS DA SEMANA',
        'body':email_template('Relatorio De Cargas Atrasadas', table_html,f"""
            <span>Resumo atrasos:</span>
                <ul>
                    <li>Pedidos atrasados da semana: {delayed_orders}</li>
                    <li>Percentual de atrasos: {delayed_percentage} %</li>
                </ul>           
        """)
        
    }
    return message