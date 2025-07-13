from src.utils.import_spreadsheet import import_spreadsheet

worksheet = import_spreadsheet('data/p.xlsx')

def read_spreadsheet():
    print('Hello world')
    for ws in worksheet:
        entregues = ws[ws['Status'] == 'Entregue']
        print(entregues)
    