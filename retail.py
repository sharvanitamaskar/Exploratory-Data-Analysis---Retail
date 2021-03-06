# -*- coding: utf-8 -*-
"""Retail.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c27rQcz4CaWgp2wOJMYkel8dTOIBiiwx
"""

# Commented out IPython magic to ensure Python compatibility.
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

from google.colab import files
uploaded = files.upload()

df = pd.read_csv(io.BytesIO(uploaded['SampleSuperstore.csv']))
print(df)

df.head

df.tail()

df.nunique

df.dtypes

df.corr()

df.shape

df.describe()

df.isnull().sum()

df.info()

df.isnull()

df["Ship Mode"].value_counts()

df["Segment"].value_counts()

df["Country"].value_counts()

df["City"].value_counts()

df["State"].value_counts()

df["Category"].value_counts()

df["Sub-Category"].value_counts()

df.drop(["Country","Postal Code"],axis=1,inplace=True)

df.head(5)

plt.figure(figsize =(8,6))
sns.heatmap(df.corr(),annot =True,cmap = 'YlOrRd')
plt.show()

sns.pairplot(df)

df_numeric = df.select_dtypes(include='number')
df_numeric.plot(kind = 'kde',subplots = True, layout = (2,2), sharex = False, figsize = (15,10))
plt.show()

p = df.groupby(by ='Segment')[['Profit']].sum()
r = p.sort_values(by = ['Profit'],ascending = True)
r.plot(kind = 'bar',figsize =(9,5),color='magenta')
plt.show()

plt.figure(figsize=(10, 7))
sns.barplot(x="Region", y="Sales", hue="Segment", data=df,palette='rainbow')
plt.show()

plt.figure(figsize =(8,6))
df.groupby(by ='Region')['Profit'].sum().plot(kind = 'pie',autopct='%1.1f%%',explode=(0.1, 0, 0,0),colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'])
plt.show()

plt.figure(figsize=(10, 7))
sns.barplot(x="Region", y="Sales", hue="Category", data=df,palette="rocket_r")
plt.show()

subcategory_grpby = df.groupby(by ='Sub-Category')[['Sales','Profit']].sum()
sort_profit2 = subcategory_grpby.sort_values(by = ['Profit'],ascending = True)
sort_profit2.plot(kind = 'bar',figsize =(13,7))
plt.show()

plt.figure(figsize=(15,8))
sns.countplot(x='Sub-Category',data=df,palette='rainbow')
plt.xticks(rotation=90)
plt.show()

df.groupby(by ='City')['Profit'].sum().sort_values(ascending = False)[521:].plot(kind = 'bar',color='green')
plt.show()

df.groupby(by ='City')['Profit'].sum().sort_values(ascending = False)[:11].plot(kind = 'bar',color='yellow')
plt.show()

plt.figure(figsize =(20,12))
df.groupby(by ='State')['Profit'].sum().sort_values(ascending = True).plot(kind = 'bar')
plt.show()

plt.figure(figsize=(12,5))
sns.lineplot(x='Discount',y='Profit',data=df)
plt.title("Discount and Profit")

plt.figure(figsize=(12,8))
sns.lineplot(x='Discount',y='Sales',data=df)
plt.title('Discount VS Sales')

df[['Discount','Profit']].corr()
#There is a negative correlation between Discount and Profit as discount increases Profit decreases