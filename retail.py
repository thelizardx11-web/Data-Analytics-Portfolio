# csv_read 
import pandas as pd 

df = pd.read_csv("retail_sales_dataset.csv")
print(df.head()) 

# check null values 
print("\nNull values:")
print(df.isnull().sum())

# drop missingg values.
df = df.dropna()

# remove duplicates 
df = df.drop_duplicates()

print("\nMissing values")
print(df.head())