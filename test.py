

import pandas as pd
import numpy
import openpyxl


loc = (r'automation_groups.xlsx')

df = pd.read_excel(loc,sheet_name='Foglio1')

xl_key = df['key']

print(xl_key)