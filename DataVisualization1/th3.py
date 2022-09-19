# Phân tích sự biến đổi số lượng đơn hàng theo thời gian
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('OnlineRetail.csv')
print(df.info())

# 1.Chọn mục tiêu Vẽ biểu đồ đường thể hiện xu hướng thay đổi số lượng 
# đơn hàng theo thời gian trong năm 2011.

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
# print(df['InvoiceDate'])
d1 = df[['InvoiceNo', 'InvoiceDate']]
d1.drop_duplicates(subset='InvoiceNo', keep='first')
# print('d11', d1)
d1 = d1.set_index(['InvoiceDate'])
# print('d12', d1)
d2 = d1.loc['2011']
d2 = d2.reset_index()
# print('d2', d2)
d3 = d2.groupby(by=d2['InvoiceDate'].dt.date).count()
# print('d3', d3)

# x = d3.index.get_level_values(0)
# plt.plot(x, d3['InvoiceDate'])
# plt.title('Number of Invoices in 2011 (Daily)', fontsize = 16)
# plt.xlabel('Date', fontsize = 14)
# plt.ylabel('#Invoices', fontsize = 14)
# plt.show()


# 2.Vẽ biểu đồ cột so sánh số lượng đơn hàng trong các tháng của năm 2011.
d4 = d2.groupby(by=d2['InvoiceDate'].dt.month).count()
# print(d4)
x = d4.index.get_level_values(0)
print(x)
plt.bar(x, d4['InvoiceDate'], tick_label = ['1','2','3','4','5','6','7','8','9','10','11','12'])
plt.title('Number of Invoices in 2011 (monthly)', fontsize = 16)
plt.xlabel('Month', fontsize = 14)
plt.ylabel('#Invoices', fontsize = 14)
plt.show()
