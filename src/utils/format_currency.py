#Formata valores decimais para o padrão brasileiro( R$ 00.000,00)
def format_currency(value):
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
