import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping

class NeuralNetwork:
    def __init__(self, input_shape, x_train, y_train):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Flatten(shape=input_shape),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(1, activation='softmax')
        ])
        early_stop = EarlyStopping(monitor='val_loss', patience=50, restore_best_weights=True)
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        self.x_train = x_train
        self.y_train = y_train


    def train(self, x_train, y_train, epochs=100):
        self.model.fit(x_train, y_train, epochs=epochs)

    def predict(self, x):
        return self.model.predict(x)
    
    def evaluate(self, x_test, y_test):
        return self.model.evaluate(x_test, y_test)

