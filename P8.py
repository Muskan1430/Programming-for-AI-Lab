# -----------------------------------
# Practical -8
# Text Classification using RNN
# -----------------------------------

# Step 1: Import Libraries
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Step 2: Sample Dataset
texts = [
    "I love this movie",
    "This film is terrible",
    "Amazing experience",
    "Worst movie ever",
    "I enjoyed the film",
    "I hate this movie"
]

labels = [1, 0, 1, 0, 1, 0]   # 1 = Positive, 0 = Negative


# Step 3: Tokenization
tokenizer = Tokenizer(num_words=1000)
tokenizer.fit_on_texts(texts)

sequences = tokenizer.texts_to_sequences(texts)


# Step 4: Padding
max_len = 5
X = pad_sequences(sequences, maxlen=max_len)
y = np.array(labels)


# Step 5: Build RNN Model
model = Sequential()

model.add(Embedding(input_dim=1000, output_dim=16, input_length=max_len))
model.add(SimpleRNN(32))
model.add(Dense(1, activation='sigmoid'))

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.summary()


# Step 6: Train Model
model.fit(X, y, epochs=10, batch_size=2)


# Step 7: Test Model
test_text = ["I really love this film"]

test_seq = tokenizer.texts_to_sequences(test_text)
test_pad = pad_sequences(test_seq, maxlen=max_len)

prediction = model.predict(test_pad)

if prediction[0][0] > 0.5:
    print("Positive Review")
else:
    print("Negative Review")