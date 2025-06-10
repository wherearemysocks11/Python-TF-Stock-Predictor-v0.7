import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # Disable GPU

class NeuralNetwork:
    def __init__(self, input_shape):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=input_shape),  # Changed from Flatten(input_shape)
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(16, activation='relu'),
            tf.keras.layers.Dense(8, activation='relu'),
            tf.keras.layers.Dense(1)
        ])
        adam = tf.keras.optimizers.Adam(learning_rate=0.000001)
        self.model.compile(optimizer=adam, loss='mean_squared_error', metrics=['mae', 'mse'])

    def train(self, x_train, y_train, x_val, y_val, epochs=100):
        early_stop = EarlyStopping(monitor='val_loss', patience=25, restore_best_weights=True)
        history = self.model.fit(x_train, y_train, epochs=epochs, callbacks=early_stop, validation_data=(x_val, y_val))
        return history  # Return training history

    def predict(self, x_test):
        return self.model.predict(x_test)
    
    def evaluate(self, x_test, y_test):
        return self.model.evaluate(x_test, y_test)

