import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_excel('house_price_dống-da.xlsx')
# print(df.head())

df_np = df[df['type_of_land'] == 'Bán nhà mặt phố']
# print(df_np.head())
df_np['price/m2'] = df_np['price'] / df_np['area']
# df_np['price/m2'].hist()
# plt.show()

df_tn = df[df['type_of_land'] == 'Bán nhà riêng']
print(df_tn.head())
df_tn['price/m2'] = df_tn['price'] / df_tn['area']
print(df_tn['price/m2'].describe())
# df_tn['price/m2'].hist()
# plt.show()

# Kiểm định giả thuyết giá (triệu đ/m2) nhà mặt phố cao hơn giá nhà trong ngõ với mức ý nghĩa 5%
print(stats.ttest_rel(df_np['price/m2'],df_tn['price/m2'] ))
# nhận H0 => nhà mặt phố giá /m2 cao hơn