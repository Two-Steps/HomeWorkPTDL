import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('shopeep_koreantop_clothing_shop_data.csv')
print(df.columns)
gr_year = df.groupby('join_year')['shopid'].agg('count')
gr_month = df.groupby(['join_year','join_month'])['shopid'].agg('count')
# print(gr_year.index)
# print(gr_month)
# plt.bar(gr_year.index, gr_year.values)
# plt.show()

# gr_month.plot(kind= 'bar')
# plt.show()

plt.scatter(x = 'response_rate', y = 'rating_good', data= df)
plt.show()
