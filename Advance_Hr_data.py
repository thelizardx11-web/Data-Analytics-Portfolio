# dataset load + EDA
import pandas as pd

df = pd.read_csv("hr_data.csv")   # apna file name

print(df.head())
print(df.info())
print(df.describe())
print(df.columns)

# encoding department 
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df["deparment_encoded"] = le.fit_transform(df["deparment"])

# crate simple target (High / Low salary)
median_salary = df["total_salary"].median()

df["salary_level"] = (df["total_salary"] > median_salary).astype(int)
# 1 = High salary, 0 = Low salary

# Train-Test-Split
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

X = df[["deparment_encoded"]]
y = df["salary_level"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


# confusion matrix 
import seaborn as sns
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)

sns.heatmap(
    cm, annot=True, fmt="d", cmap="Blues",
    xticklabels=["Low Salary", "High Salary"],
    yticklabels=["Low Salary", "High Salary"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("HR Salary Level Classification")
plt.show()
