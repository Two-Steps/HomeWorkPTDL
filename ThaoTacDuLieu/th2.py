# Tách dữ liệu của một cột thành nhiều cột
import pandas as pd
import numpy as np

df = pd.read_csv('shopeep_koreantop_clothing_shop_data.csv')
# print(df)
# print(df.columns)
# ['pk_shop', 'date_collected', 'shopid', 'name', 'join_month', 'join_day',
# 'join_year', 'item_count', 'follower_count', 'response_time',
# 'response_rate', 'shop_location', 'rating_bad', 'rating_good',
# 'rating_normal', 'rating_star', 'is_shopee_verified',
#  'is_official_shop']

# - Để đơn giản ta lấy vài thuộc tính
df = df[['date_collected', 'shop_location', 'response_time']]
# print(df.head())
print(df.info())

# - Tách cột dùng split()
# Tách cột shop_location thành 2 cột District và City
df['District'] = df['shop_location'].str.split(',').str[0]
df['City'] = df['shop_location'].str.split(',').str[1]
# print(df.head())

# - Tách cột dữ liệu có kiểu ngày tháng
# Tách cột date_collected thành 3 cột Day, Month, Year
df['Day'] = pd.to_datetime(df['date_collected'], format='%Y-%m-%d').dt.day
df['Month'] = pd.to_datetime(df['date_collected'], format='%Y-%m-%d').dt.month
df['Year'] = pd.to_datetime(df['date_collected'], format='%Y-%m-%d').dt.year
# print(df.head())

# - Tách cột dữ liệu có kiểu thời gian
# Tách cột response_time thành 3 cột Hours, Minute, Second
df['Hours'] = pd.to_datetime(df['response_time'], format=' %H:%M:%S').dt.hour
df['Minute'] = pd.to_datetime(df['response_time'], format=' %H:%M:%S').dt.minute
df['Second'] = pd.to_datetime(df['response_time'], format=' %H:%M:%S').dt.second
print(df.head())
