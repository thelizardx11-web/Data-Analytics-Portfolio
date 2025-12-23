# import libararies 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# load dataset 
df = pd.read_csv("penguins.csv")

# basic exploration 
print(df.head())
print(df.info())
print(df.describe())

# missing value check 
print(df.isnull().sum())

# data cleaning 
df_clean = df.dropna().copy()
print("clean shape:", df_clean.shape)

# encode target column 
le_species = LabelEncoder()
df_clean["species_label"] = le_species.fit_transform(df_clean["species"])

print(df_clean["species"].value_counts())

# simple visulization (EDA)
'''plt.figure(figsize=(6,4))
sns.boxplot(x="species", y="flipper_length_mm", data=df_clean)
plt.title("Flipper Length by Species")
plt.show()'''

# Scatter plot: flipper length vs body mass
'''plt.figure(figsize=(6,4))
sns.scatterplot(
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species",
    data=df_clean
)
plt.title("Flipper Vs Body mass")
plt.show()'''

# feature selection 
feature_cols = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g"
]

X = df_clean[feature_cols]
y = df_clean["species_label"]

# Train test split (Startieied)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Random forest model traning 
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)


# Predications + evalution 
y_pred = rf_model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(
    y_test,
    y_pred,
    target_names=le_species.classes_
))


# CONFUSION matrix 
'''cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,4))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=le_species.classes_,
    yticklabels=le_species.classes_
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion matrix - Penguins Species")
plt.show()'''

# Feature importance (Top 5)
importances = rf_model.feature_importances_

feature_importance_df = pd.DataFrame({
    "Feature": feature_cols,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

plt.figure(figsize=(6,4))
sns.barplot(
    x="Importance",
    y="Feature",
    data=feature_importance_df
)
plt.title("Feature Importance - Random Forest")
plt.show()

print(feature_importance_df)
