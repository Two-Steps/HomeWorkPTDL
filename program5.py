# ghi dữ liệu vào dataframe
import pandas as pd

df = pd.read_csv('FoodPrice_in_Turkey.csv')
print(df.head())

# # ghi dữ liệu vào file csv
# df.to_csv('demo_FoodPrice.csv')

# # ghi dữ liệu vào file excel
# df.to_excel('demo_FoodPrice.xlsx')

# # ghi dữ liệu vào file Json
# df.to_json('demo_FoodPrice.json', orient='columns')

# # ghi dữ liệu vào file hdf5
# df.to_hdf('demo_FoodPrice.hdf', 'table')

# ghi dữ liệu vào file html
df.to_html('demo_FoodPrice.html')