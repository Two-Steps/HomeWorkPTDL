import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("OnlineRetail.csv", encoding = "ISO-8859-1")
print(df.info())
df = df.dropna()
df["Price"] = df["Quantity"] * df["UnitPrice"]
sns.violinplot(y = "UnitPrice", data=df)
sns.violinplot(y = "Price", data=df)

df2 = df.groupby(['InvoiceNo'])['Quantity'].sum().reset_index()
sns.violinplot(y="Quantity", data=df2)

df3 = df.groupby(['Country'])['Quantity'].sum().reset_index()
df1 = df.drop_duplicates(subset = 'InvoiceNo')
sns.countplot(x = "Country", data = df1)
plt.show()