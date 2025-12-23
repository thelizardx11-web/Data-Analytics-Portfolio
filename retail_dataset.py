import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 

# loaded dataset 
df = pd.read_csv("retail_sales_dataset.csv")

# preview data 
print("\n===== Data Head =====")
print(df.head())

# check dataset shape 
print("\n===== SHAPE =====")
print(df.head())

# check missing values 
print("\n===== Missing Values =====")
print(df.isnull().sum())

# handle missing values 
df.fillna(method='ffill', inplace=True)

# Data summary 
print("\n===== SUMMARY =====")
print(df.describe())

# Data types 
print("\n===== Data Types =====")
print(df.types)

# check duplicates rows 
duplicates = df.duplicated().sum()
print(f"\n===== DUPLICATES FOUND: {duplicates} =====")

if duplicates > 0:
    df.drop_duplicates(inplace=True)
    print("Duplicates removed.")


# Bar Chart Example — change column names if different
if "Product" in df.columns:
    df["Product"].value_counts().head(10).plot(kind='bar')
    plt.title("Top 10 Most Sold Products")
    plt.xlabel("Product")
    plt.ylabel("Count")
    plt.show()

print("\n===== PROCESS COMPLETE 🚀 =====")

plt.figure(figsize=(10,5))
df['Product'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Most Selling Products")
plt.xlabel("Product Name")
plt.ylabel("Sales Count")
plt.xticks(rotation=45)
plt.show()
