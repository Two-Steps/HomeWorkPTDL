import pandas as pd
import numpy as np

df = pd.read_csv('OnlineRetail.csv')
# print(df.columns)
# ['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',
# 'UnitPrice', 'CustomerID', 'Country']

# print('Số dòng: ' + str(df.shape[0]) )
# print('Số cột: ' + str(df.shape[1]) )
# print(df.info())

# 2.Tạo cột mới quý 'Previous'
# nhận gtri 1 nếu ngày lập hóa đơn trong các tháng 1,2,3
# nhận gtri 2 nếu ngày lập hóa đơn trong các tháng 4,5,6
# nhận gtri 3 nếu ngày lập hóa đơn trong các tháng 7,8,9
# nhận gtri 4 nếu ngày lập hóa đơn trong các tháng 10,11,12
df['month'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.month

conditions = [(df['month'] <= 3),
                (df['month'] <= 6) & (df['month'] > 3),
                (df['month'] <= 9) & (df['month'] > 6)]
choices_ = [1, 2, 3]
df['Previous'] = np.select(conditions, choices_, default=4)
# df = df[['month', 'Previous']]

# 3. Tạo cột 'Amount' = Quantity * UnitPrice
df['Amount'] = df['Quantity'] * df['UnitPrice']

# 4. Tạo cột 'Discount' 
# nếu Country là 'United Kingdom' và thuộc quý 4 thì 10%
# 5% nếu là 'France' ngược lại là 0%

condition2 = [(df['Country'] == 'United Kingdom') & (df['Previous'] == 4),
            (df['Country'] == 'France') & (df['Previous'] == 4)]

choices_2 = ['10%', '5%']
df['Discount'] = np.select(condition2, choices_2, default='0%')

# 5. Tạo cột mới 'Total' nhận giá trị = Amount - Discount
# df['Discount'] = df['Discount'].str.slice(stop=-1)
df['Total'] = df['Amount'] - df['Amount'] * df['Discount'].str.slice(stop=-1).astype('int32')/100
print(df)
