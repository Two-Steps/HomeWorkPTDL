# Thực hành đọc dữ liệu vào DataFrame
import pandas as pd 
import numpy as np

# df = pd.read_csv('FoodPrice_in_Turkey.csv')
# df.head()

# df = pd.read_excel('house_price_dống-da.xlsx')
# df.head()

# df = pd.read_json('house_price_json.json')
# df.head()

url = 'https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_North_America'
df = pd.read_html(url)
print(df[0].head(5))