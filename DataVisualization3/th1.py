import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("FoodPrice_in_Turkey.csv")
print(df.info())
df = df.dropna()
rice_df = df[df["ProductId"] == 52]
sns.lmplot(x="Year", y="Price",data = rice_df)
trans_df = df[(df["ProductName"] == "Transport (public) - Retail") | (df["ProductName"] == "Rice - Retail")]
sns.lmplot(x="Year", y="Price", hue="ProductName", data = trans_df)
sns.violinplot(y = "Price", data=df)
sns.violinplot(y = "Year", data=df)
sns.countplot(x = "Year", data = df)
sns.countplot(x = "Place", data = df)
sns.countplot(x = "Year", hue = "Place", data = df)
plt.show()