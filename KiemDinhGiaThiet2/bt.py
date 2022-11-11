import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_excel('house_price_dống-da.xlsx')
print(df.info())
df1 = df.dropna(subset=['price', 'area'])
# Giữa giá nhà và diện tích có tương quan với nhau?
print(stats.pearsonr(df1['price'], df1['area']))
# (0.16338660074802464, 4.6087480328406026e-07)
# vì r < 0.05 nên giá nhà có tương quan với diện tích

# Giữa giá nhà và tọa độ địa lý (lat, long) có tương quan với nhau
df2 = df.dropna(subset=['lat', 'long'])
print(stats.pearsonr(df2['lat'], df2['long']))
# không tương quan

# Giữa thuộc tính land_certificate và property_type có tương quan với nhau
df3 = df.dropna(subset=['land_certificate', 'type_of_land'])
contigency= pd.crosstab(df3['land_certificate'], df3['type_of_land'])
c, p, dof, expected = stats.chi2_contingency(contigency)
print(p)
# vì p = 1 nên bác bỏ H0 => có mối liên hệ
# Giả thuyết không: giữa hai thuộc tính không có mối liên hệ
# Giả thuyết đối: Giữa hai thuộc tính có mối liên hệ