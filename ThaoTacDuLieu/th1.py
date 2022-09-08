# Thêm cột dữ liệu mới từ các cột dữ liệu đã có
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

# -Đơn giản hóa việc lọc tập dữ liệu bằng cách chọn vài cột thôi :))
df = df[['join_month', 'join_day', 'join_year', 'shop_location',
    'rating_bad', 'rating_good', 'rating_normal']]
# print(df)

# -Tạo cột 'rating' tính điểm cho mỗi cửa hàng dựa vào thông tin rating_bad, 
# rating_good, rating_normal
# công thức: rating = rating_good*2 + rating_normal - rating_bat*3

df['rating'] = df['rating_good']*2 + df['rating_normal'] - df['rating_bad']*3
# print(df)

# -Thêm cột mới từ các cột có kiểu chuỗi
# sử dụng astype(str) -> convert về kiểu chuỗi
# ghép 3 cột tháng ngày năm thành cột mới 'date'
df['date'] = df['join_month'] + ' ' + df['join_day'].astype(str) \
            + ',' + df['join_year'].astype(str)
# print(df)

# -Thêm cột mới theo điều kiện
# Thêm cột new có giá trị True nếu join_year = 2021, ngược lại False
df['new'] = df['join_year'] == 2021
# print(df)

# Thêm cột rate có giá trị good nếu rating_good >= 5000, còn lại bad
df['rate'] = np.where(df['rating_good'] >= 5000, 'good', 'bad')
# print(df)

# Nếu có nhiều hơn 2 lựa chọn ta sử dụng np.select
# Thêm cột flag tặng cờ cho các cửa hàng, flag nhận các giá trị như sau:
# blue khi rating_good >= 30000 và rating_bad <= 100
# yellow khi 10000 <= rating_good < 30000 và 100 < rating_bad <= 1000
# red khi rating_good < 10000
# black đối với các trường hợp còn lại
conditions1 = [(df['rating_good'] >= 30000) & (df['rating_bad'] <= 100),
                (df['rating_good'] < 30000) & (df['rating_good'] >= 1000) &
                (df['rating_bad'] > 100) & (df['rating_bad'] <= 1000)
                ,(df['rating_good'] < 10000)]

choices1 = ['blue', 'yellow', 'red']
df['flag'] = np.select(conditions1, choices1, default='black')
print(df)