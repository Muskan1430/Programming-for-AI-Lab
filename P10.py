# -----------------------------------
# Practical -10
# Simple Deep Neural Network (DNN)
# -----------------------------------

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris


# ===============================
# Step 2: Load Dataset
# ===============================

data = load_iris()

X = data.data
y = data.target

# One-hot encoding
y = to_categorical(y, num_classes=3)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


# ===============================
# Step 3: Build Model
# ===============================

model = Sequential()

# Input + Hidden Layer
model.add(Dense(16, input_dim=4, activation='relu'))

# Hidden Layer
model.add(Dense(12, activation='relu'))

# Output Layer
model.add(Dense(3, activation='softmax'))


# ===============================
# Step 4: Compile Model
# ===============================

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)


# ===============================
# Step 5: Train Model
# ===============================

history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=5,
    validation_split=0.2
)


# ===============================
# Step 6: Evaluate Model
# ===============================

loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)


# ===============================
# Step 7: Prediction
# ===============================

prediction = model.predict(X_test[:1])
print("Predicted Class:", np.argmax(prediction))