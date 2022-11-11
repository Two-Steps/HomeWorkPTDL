import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_excel('house_price_dống-da.xlsx')
print(df.info())
df['toilet'].interpolate(method= 'linear', inplace= True)
df['bedroom'].interpolate(method= 'linear', inplace= True)
is_na = df['area'].notna()
df = df[is_na]
is_na2 = df['price'].notna()
df = df[is_na2]

# sns.scatterplot(x= df['price'], y = df['area'])
# sns.scatterplot(x= df['price'], y = df['toilet'])
# sns.scatterplot(x= df['price'], y = df['bedroom'])
# plt.show()

house_direc = df[df['house_direction'].notna()]
house_direc = house_direc.groupby('house_direction')['price'].agg('mean')
sns.barplot(x = house_direc.index, y = house_direc.values)
plt.show()