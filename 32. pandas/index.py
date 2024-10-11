import pandas as pd # we can also do import pandas, the pd is an alias

# 1D labeled array 
series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
# print(series)


#  2D table, with labeled rows and columns.
data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'Salary': [50000, 60000, 70000]
        }

df = pd.DataFrame(data)
print(df.loc[2])

#pandas version 
# print(pd.__version__)



# Importing data from CSV:
# df = pd.read_csv('data.csv')
# print(df.head())

# pip install openpyxl
# # Importing data from Excel:
# df = pd.read_excel('data.xlsx')
# print(df.head())




