import xlrd

sheets = ['Sheet1', 'Sheet2']

def extract_xl_col_names(path, sheet_name):
    
    # To open Workbook
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_name(sheet_name)

    # 1st row values
    print(sheet.row_values(0))

for sheet in sheets:
    extract_xl_col_names("C://Users//User//Desktop//Book1.xlsx", sheet)
