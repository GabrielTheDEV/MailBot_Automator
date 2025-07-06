 
import pandas as pd
from pandas import DataFrame

# Leitor de planilha
def read_Spreadsheet(path: str) -> DataFrame:
    try:
        return pd.read_excel(path)
    except Exception as err:
        print(f"[ ERRO ]: Falha ao tentar ler a planilha {err}")
        raise