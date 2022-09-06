# phân tích trên bộ dữ liệu Online Retail
import pandas as pd
import numpy as np

df = pd.read_csv('OnlineRetail.csv')
print(df.head())
# print(df.columns)
# ['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',
#        'UnitPrice', 'CustomerID', 'Country']

# print('Số dòng: ' + str(df.shape[0]))
# print('Số cột: ' + str(df.shape[1]))
# print(df.info())

# # -Trích xuất dữ liệu các cột Description và Quantity lưu vào file OnlineRetail1.csv
# df1 = df.loc[:, ['Description', 'Quantity']]
# df1.to_csv('OnlineRetail1.csv')

# # -Trích xuất dữ liệu 1000 dòng đầu tiên lưu vào file OnlineRetail1.xlsx
# df2 = df.iloc[:1000]
# df2.to_excel('OnlineRetail1.xlsx')

# -Trích xuất các bản ghi có số lượng từ 10 trở lên lưu vào file OnlineRetail1.h5
# df3 = df.loc[df['Quantity'] >= 10]
# df3.to_hdf('OnlineRetail.hdf', 'table')

# -Trích xuất dữ liệu các phần tử từ dòng 1000 đến dòng 2000, 
# các cột Quantity, InvoiceDate, UnitPrice lưu vào file OnlineRetail1.json
# df4 = df.loc[1000:2000, ['Quantity', 'InvoiceDate', 'UnitPrice']]
# df4.to_json('OnlineRetail1.json')

# -Trích xuất các bản ghi có số hóa đơn ‘536365’ lưu vào file OnlineRetail1.html
df5 = df.loc[df['InvoiceNo'] == '536365']
df5.to_html('OnlineRetail1.html')

