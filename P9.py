# -----------------------------------
# Practical -9
# Image Classification using CNN
# -----------------------------------

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense


# ===============================
# Step 2: Load Dataset
# ===============================

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize
X_train = X_train / 255.0
X_test = X_test / 255.0

# Reshape for CNN (4D input)
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)


# ===============================
# Step 3: Build CNN Model
# ===============================

model = Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))


# ===============================
# Step 4: Compile Model
# ===============================

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)


# ===============================
# Step 5: Train Model
# ===============================

model.fit(X_train, y_train, epochs=2, batch_size=64)


# ===============================
# Step 6: Evaluate Model
# ===============================

test_loss, test_accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", test_accuracy)


# ===============================
# Step 7: Prediction
# ===============================

prediction = model.predict(X_test[:1])
print("Predicted Digit:", np.argmax(prediction))