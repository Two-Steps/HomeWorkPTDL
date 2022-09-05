# phân tích dữ liệu GDP list
import pandas as pd

df = pd.read_csv('GDPlist.csv', encoding='latin1')

# print(df.info())
print('số dòng: ' + str(df.shape[0]))
print('số cột: ' + str(df.shape[1]))

# print(df.head())
# mỗi châu lục có bao nhiêu quốc gia nằm trong bảng dữ liệu
continent = df.groupby(['Continent'])['Country'].count()
print('Số quốc gia của mỗi châu lục: ', continent.head(), sep='\n')

# tổng GDP của từng châu lục
print(' ' * 30)
total_gdp = df.groupby('Continent')['GDP (millions of US$)'].sum()
print('Tổng GDP của từng châu lục:', total_gdp.head(), sep='\n')

# top 10 quốc gia có GDP cao nhất
print(' ' * 30)
df.columns = ['Country', 'Continent', 'GDP']
df.sort_values(by='GDP', ascending=False, inplace=True)
print(df.head(10))
