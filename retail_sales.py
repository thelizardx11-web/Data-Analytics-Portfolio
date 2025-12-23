# csv_read
import pandas as pd
import numpy as np 

# load dataset 
df = pd.read_csv("retail_sales_dataset.csv", encoding='latin1')

# basic info 
print("Dataset Preview:")
print(df.head())

print("\n Dataset Info:")
print(df.info())

# missing values check 
print("\nMissing Values in each column:")
print(df.isnull().sum())

# Handling missing  Values 
# fill  numeric missing with median & categorical with mode 
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nAfter Filling Missing Values:")
print(df.isnull().sum())

# --------- Convert Date Column ----------
# Change column name accordingly (example: 'InvoiceDate' or 'Date')
df['Date'] = pd.to_datetime(df['Date'])

print("\nDate Converted Successfully")

# --------- Feature Engineering ----------
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
df['Revenue'] = df['Quantity'] * df['Price per Unit']  # Change name if different

print("\nNew Columns Added:")
print(df.head())

# --------- Check Duplicates ----------
print("\nDuplicate Records:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicates Removed")

# --------- Outlier Check ----------
print("\nOutlier Summary:")
print(df.describe())

