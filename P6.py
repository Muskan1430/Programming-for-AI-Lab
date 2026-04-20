# -----------------------------------
# Practical -6
# Ensemble Learning Models
# -----------------------------------

# Step 1: Import Libraries
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC


# Step 2: Load Dataset
X, y = load_breast_cancer(return_X_y=True)


# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


# ===============================
# PART A: Random Forest
# ===============================

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)
print("Random Forest Accuracy:", accuracy_score(y_test, rf_pred))


# ===============================
# PART B: Gradient Boosting
# ===============================

gb_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
gb_model.fit(X_train, y_train)

gb_pred = gb_model.predict(X_test)
print("Gradient Boosting Accuracy:", accuracy_score(y_test, gb_pred))


# ===============================
# PART C: Stacking Classifier
# ===============================

# Base Models
estimators = [
    ('rf', RandomForestClassifier(n_estimators=50, random_state=42)),
    ('svm', SVC(probability=True))
]

# Stacking Model
stack_model = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression()
)

# Train & Evaluate
stack_model.fit(X_train, y_train)
stack_pred = stack_model.predict(X_test)

print("Stacking Model Accuracy:", accuracy_score(y_test, stack_pred))