import pandas as pd

def import_spreadsheet(path: str) -> pd.DataFrame:
    try:
        with open(path , 'rb') as file:
            try:
                return pd.read_excel(file)
            except Exception as e:
                print(f"Erro inesperado: {e}")

    except FileNotFoundError:
        print("Erro: o arquivo não foi encontrado.")
    except ValueError:
        print("Erro: tipo de arquivo inválido ou formato incorreto.")
   
    