import pandas as pd
from scipy import  stats

df = pd.read_csv("shopeep_koreantop_clothing_shop_data.csv", encoding="UTF-8")
df1 = df.filter(["rating_star", "follower_count"])
df1 = df1.dropna()
print(stats.pearsonr(df1.rating_star, df1.follower_count))

# Giữa rating_star và số lượng sản phẩm (item_count) có tương quan với nhau hay không
# rating_star và item_count là hai thuộc tính định lượng, sử dụng kiểm định pearson để kiểm định mức độ tương quan giữa hai thuộc tính
# Giả thuyết không: Giữa hai thuộc tính không có sự tương quan tuyến tính
# Giả thuyết đối: Giữa hai thuộc tính có sự tương quan tuyến tính
df1 = df.filter(["rating_star", "item_count"])
df1 = df1.dropna()
print(stats.pearsonr(df1.rating_star, df1.item_count))

