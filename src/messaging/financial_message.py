from src.utils.read_worksheet import read_worksheet
from src.templates.emails_template import email_template
from src.utils.format_currency import format_currency

def financial_message() -> dict:
    data = read_worksheet()

    columns = [
        'Data de emissão','Carga','Cliente','Origem',
        'Destino','Status','Valor Frete, Status de Pagamento'
    ]
    total_billed : float = data['Valor Frete'].sum()
    payments_received : float = data.loc[data['Status'].isin(['Atrasada', 'Em trânsito']), 'Valor Frete'].sum()
    pending_payments : float = data[data['Status'] == 'Entregue']['Valor Frete'].sum()

    if all(c in data.columns for c in columns):
        data = data[columns]

    table_html = data.to_html(index=False, border=1)

    message = {
        'subject':'RELATORIO FINANCEIRO DA SEMANA',
        'body': email_template('Segue o relatorio financeiro da semana', table_html, f"""
            <span>Resumo Financeiro:</span>
                <ul>
                    <li>Total faturado na semana: {format_currency(total_billed)}</li>
                    <li>Pagamentos recebidos: {format_currency(payments_received)}</li>
                    <li>Pagamentos pendentes: {format_currency(pending_payments)}</li>
                </ul>           
        """)
    }
    return message