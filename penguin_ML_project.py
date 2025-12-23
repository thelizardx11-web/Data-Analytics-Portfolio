# imp libaries 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# step 1. loadede dataset 
df = pd.read_csv("penguins.csv")
print("sucessfully print!")
print(df.head())

# Quick peak 
print("INFO:")
print(df.info(), "\n")
print("DESCRIBE:")
print(df.describe(include='all'), "\n")

# step 2. missing values 
print("Missing values per column:")
print(df.isnull().sum(), "\n")

# simple cleaning startegy;
df_clean = df.dropna().reset_index(drop=True)
print(f"Rows before: {len(df)}, after dropna(): {len(df_clean)}\n")

# step 3. Encoding categorical columns 
le = LabelEncoder()
df_clean ['species_label'] = le.fit_transform(df_clean['species']) # 0,1,2  encoding 
print("Label encoding mapping (species -> lable):")
for lab, cls in enumerate(le.classes_):
    print(lab, "=", cls)
print()

# one handeded encod 'island'
df_encoded = pd.get_dummies(df_clean, columns=['island'], drop_first=True) # drop_first to avoid collinetly 

# chose features (3-6 numeric/encoded columns)
feature_cols = [
    'bill_length_mm',
    'bill_depth_mm',
    'flipper_length_mm',
    'body_mass_g'
]

# add island dummies if present 
island_cols = [c for c in df_encoded.columns if c.startswith('island_')]
feature_cols += island_cols

# final feature matrix and target 
X = df_encoded[feature_cols].copy()
y = df_encoded['species_label'].copy()

print("Final features used:")
print(feature_cols)
print("\nFeature sample:")
print(X.head(), "\n")

# Train / Test split 
X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size=0.20, random_state=42, stratify=y
)

print(f"Train shape; {X_train.shape}, Test shape: {X_test.shape}\n")

# step 5. model: Randomforestclassifier 
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# predict + evaluate 
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", round(acc, 4))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# step 6. confusion matrix plot
'''cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=le.classes_, yticklabels=le.classes_)
plt.title('Confusion Matrix (RandomForest)')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.show()'''

# step 7 feature importance (bar chart)
importances = model.feature_importances_
feat_names = X.columns.tolist()
fi_df = pd.DataFrame({'feature': feat_names, 'importance': importances}).sort_values('importance', ascending=False)

plt.figure(figsize=(8,4))
sns.barplot(data=fi_df, x='importance', y='feature')
plt.title('Feature Importances (RandomForest)')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.tight_layout()
plt.show()

# step 8. short interpretation (print)
print("Top feature by importance:")
print(fi_df.head(), "\n")