import pandas as pd

groceries = pd.read_csv('groceries.csv')
print(groceries.head())

df2 = {'Item':'Broccoli', 'Amt':5, 'Type':'Food', 'Usage':'Daily'}
groceries = groceries.append(df2, ignore_index=True)