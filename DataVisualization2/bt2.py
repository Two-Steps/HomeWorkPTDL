import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('house_price_dống-da.xlsx')
print(df.info())
df['toilet'].interpolate(method= 'linear', inplace= True)
df['bedroom'].interpolate(method= 'linear', inplace= True)
is_na = df['area'].notna()
df = df[is_na]
is_na2 = df['price'].notna()
df = df[is_na2]

fig, ax = plt.subplots()
twin1 = ax.twinx()
twin2 = ax.twinx()
ax.plot(df['price'], df['area'], 'b', label = 'Price_Area')
twin1.plot(df['price'], df['bedroom'], 'g', label = 'Price_Bed')
twin2.plot(df['price'], df['toilet'], 'b', label = 'Price_Toilet')
ax.set_xlabel("Price")
ax.set_ylabel("Area")
twin1.set_ylabel("Bedroom")
twin2.set_ylabel("Toilet")
plt.show()
