
"""To perform data import/export (.CSV, .XLS, .TXT) operations using data frames in Python."""
import openpyxl as openpyxl
import pandas as pd
# data = pd.read_csv("/Users//nikhilpratapsingh//Desktop//student.csv")
# print(data)
# data3 = pd.read_table("/Users//nikhilpratapsingh//Desktop//Artificial Intelligence.txt")
# print(data3)
# data4 = pd.read_excel("/Users//nikhilpratapsingh//Desktop//sales.xlsx")
# print (data4)

data = {'Product': ['Desktop Computer','Tablet','Printer','Laptop'],
        'Price': [850,200,150,1300]
        }
df = pd.DataFrame(data, columns= ['Product', 'Price'])
df.to_csv ("/Users/nikhilpratapsingh/Desktop/export_dataframe.csv", index = False)
print (df)

