import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # Disable GPU

class NeuralNetwork:
    def __init__(self, input_shape, x_train, y_train):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Flatten(input_shape=input_shape),
            tf.keras.layers.Dense(128, activation='sigmoid'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        self.model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
        self.x_train = x_train
        self.y_train = y_train

    def train(self, x_val, y_val, epochs=100):
        early_stop = EarlyStopping(monitor='val_loss', patience=25, restore_best_weights=True)
        self.model.fit(self.x_train, self.y_train, epochs=epochs, callbacks=early_stop, validation_data=(x_val, y_val))

    def predict(self, x):
        return self.model.predict(x)
    
    def evaluate(self, x_test, y_test):
        return self.model.evaluate(x_test, y_test)

