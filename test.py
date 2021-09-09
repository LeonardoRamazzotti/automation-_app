

import pandas as pd
import numpy

loc = (r'automation_groups.xlsx')

df = pd.read_excel(loc,sheet_name='Foglio1')

xl_key = df['key'[1]]

print(xl_key)