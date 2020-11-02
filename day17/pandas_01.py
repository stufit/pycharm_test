import pandas as pd

accident = pd.read_csv('acci.csv',engine='python',encoding='euc-kr')
print(accident.head())



