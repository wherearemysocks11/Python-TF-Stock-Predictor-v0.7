import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
import os
import numpy as np
from config import NN_CONFIG, CUDA_VISIBLE_DEVICES

os.environ['CUDA_VISIBLE_DEVICES'] = CUDA_VISIBLE_DEVICES

class NeuralNetwork:
    def __init__(self, input_shape):
        self.model = self._build_model(input_shape)
        self._compile_model()

    def _build_model(self, input_shape):
        layers = [tf.keras.layers.Input(shape=input_shape),
                 tf.keras.layers.Flatten()]
        
        # Add dense layers from configuration
        for units in NN_CONFIG['dense_layers'][:-1]:
            layers.append(tf.keras.layers.Dense(units, activation='relu'))
        
        # Add final output layer
        layers.append(tf.keras.layers.Dense(NN_CONFIG['dense_layers'][-1]))
        
        return tf.keras.Sequential(layers)

    def _compile_model(self):
        optimizer = tf.keras.optimizers.Adam(learning_rate=NN_CONFIG['learning_rate'])
        self.model.compile(optimizer=optimizer, 
                         loss='mean_squared_error',
                         metrics=['mae', 'mse'])

    def train(self, x_train, y_train, x_val, y_val, epochs=100):
        early_stop = EarlyStopping(
            monitor='val_loss',
            patience=NN_CONFIG['early_stop_patience'],
            restore_best_weights=True
        )
        return self.model.fit(
            x_train, y_train,
            epochs=epochs,
            callbacks=[early_stop],
            validation_data=(x_val, y_val)
        )

    def predict(self, x_test, scaler, num_features):
        prediction = self.model.predict(x_test)
        prediction_reshaped = np.zeros((1, num_features))
        prediction_reshaped[0, 0] = prediction[0][0]
        return scaler.inverse_transform(prediction_reshaped)[0, 0]
    
    def evaluate(self, x_test, y_test):
        return self.model.evaluate(x_test, y_test)

