# -----------------------------------
# Practical -7
# Feature Scaling, Encoding & Selection
# -----------------------------------

# Step 1: Import Libraries
import pandas as pd
import numpy as np


# Step 2: Create Dataset
data = {
    'Age': [22, 25, 30, 35, 40],
    'Salary': [30000, 50000, 60000, 80000, 100000],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Pune', 'Mumbai'],
    'Purchased': [0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)


# ===============================
# PART A: Feature Encoding
# ===============================

# Label Encoding
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['City_Label'] = le.fit_transform(df['City'])

print("\nAfter Label Encoding:\n", df)


# One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['City'])

print("\nAfter One-Hot Encoding:\n", df_encoded)


# ===============================
# PART B: Feature Scaling
# ===============================

# Standardization
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df_encoded[['Age', 'Salary']] = scaler.fit_transform(df_encoded[['Age', 'Salary']])

print("\nAfter Standardization:\n", df_encoded)


# Normalization
from sklearn.preprocessing import MinMaxScaler

minmax = MinMaxScaler()
df_encoded[['Age', 'Salary']] = minmax.fit_transform(df_encoded[['Age', 'Salary']])

print("\nAfter Normalization:\n", df_encoded)


# ===============================
# PART C: Feature Selection
# ===============================

# Correlation
correlation = df_encoded.corr()
print("\nCorrelation with Purchased:\n", correlation['Purchased'])


# SelectKBest
from sklearn.feature_selection import SelectKBest, chi2

X = df_encoded.drop('Purchased', axis=1)
y = df_encoded['Purchased']

selector = SelectKBest(score_func=chi2, k=2)
X_new = selector.fit_transform(abs(X), y)

print("\nSelected Features Shape:", X_new.shape)


# Feature Importance (Random Forest)
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X, y)

importances = model.feature_importances_

print("\nFeature Importances:")
for feature, importance in zip(X.columns, importances):
    print(feature, ":", importance)