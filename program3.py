# phân tích dữ liệu Food Price In Turkey
import pandas as pd

df = pd.read_csv('FoodPrice_in_Turkey.csv')

print('Số dòng: ' + str(df.shape[0]))
print('Số cột: ' + str(df.shape[1]))

print('-' * 60)
print(df.columns)
print(df.head())

print('-' * 60)
# giá trung bình của từng loại thực phẩm
avg_price = df.groupby(['ProductId', 'ProductName'])['Price'].mean()
print(avg_price.head())