# import libararies 
import pandas as pd 

df = pd.read_csv("penguins.csv")
print(df.head())
print(df.info())
print(df.describe())

# MISSING VALUES 
print("MISSING values per column:")
print(df.isnull().sum())

# duplicates values 
print("Duplicates rows count:",df.duplicated().sum()) 
# optional drop duplicates 
print(df.drop_duplicates())

# import visulization
import matplotlib.pyplot as plt 
import seaborn as sns 

# bar chart 
'''plt.figure(figsize=(10,6))
sns.countplot(data=df, x='species')
plt.title('count of each Penguins species')
plt.xlabel('species')
plt.ylabel('count')
plt.show()'''

# HISTogram 
'''plt.figure(figsize=(8,6))
sns.histplot(data=df, x='island', bins=20, kde=True)
plt.title('Distribution of island')
plt.xlabel('island')
plt.ylabel('Frequency')
plt.show()'''

# scatter plot 
sns.pairplot(df, hue='species')
plt.suptitle('Pairplot of Penguins features by species', y=1.02)
plt.show()