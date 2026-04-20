# -----------------------------------
# Practical -3
# Evaluation of Classification & Regression Models
# -----------------------------------

# ===============================
# PART A: Classification
# ===============================

# Step 1: Import Libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# Step 2: Load Dataset
X, y = load_iris(return_X_y=True)


# Step 3: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


# Step 4: Train Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)


# Step 5: Prediction
y_pred = model.predict(X_test)


# Step 6: Evaluation
print("---- Classification Model ----")

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ===============================
# PART B: Regression
# ===============================

# Step 1: Import Libraries
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np


# Step 2: Load Dataset
X, y = load_diabetes(return_X_y=True)


# Step 3: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


# Step 4: Train Model
reg_model = LinearRegression()
reg_model.fit(X_train, y_train)


# Step 5: Prediction
y_pred = reg_model.predict(X_test)


# Step 6: Evaluation
print("\n---- Regression Model ----")

# MAE
print("MAE:", mean_absolute_error(y_test, y_pred))

# MSE
mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)

# RMSE
print("RMSE:", np.sqrt(mse))

# R2 Score
print("R2 Score:", r2_score(y_test, y_pred))