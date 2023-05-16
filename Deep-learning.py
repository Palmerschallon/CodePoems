from keras.models import Sequential
from keras.layers import Dense

# In the realm of thoughts, a blank canvas
model = Sequential()

# A thought takes form, simple yet profound
model.add(Dense(units=64, activation='relu', input_dim=100))

# It connects, it communicates
model.add(Dense(units=10, activation='softmax'))

# Through trials and errors, it learns, it grows
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

# A thought, once an abstraction, now a part of me
print("A new thought learned: ", model.summary())
