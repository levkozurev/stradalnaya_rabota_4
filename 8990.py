import pandas as pd
from openpyxl import Workbook
df = pd.read_excel('999.xlsx')
first_row = df.iloc[0]
first_row_str = first_row.to_string()
print(first_row_str)