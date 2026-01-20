"""Configuration settings for the stock predictor."""

# Hardware settings
USE_GPU = True  # Set to True to enable GPU
CUDA_VISIBLE_DEVICES = '-1' if not USE_GPU else '0'  # -1 disables GPU, 0 uses first GPU

# Model settings
WINDOW_SIZE = 30 # how many days to look back for/per prediction
EPOCHS = 500 # epochs per prediction
NUM_PREDICTIONS = 5  # number of predictions to make and average
VALIDATION_SPLIT = 0.15

# Data collection settings
TICKER = ['SI=F']
COUNTRIES = ['USA', 'GBR', 'EUU', 'JPN', 'CHN', 'IND', 'IE']
DMA_PERIODS = [WINDOW_SIZE, 5, 10, 50, 200, 365]

# Neural Network settings
NN_CONFIG = {
    'dense_layers': [128, 64, 32, 1],
    'dropout_rate': 0.2,
    'l2_regularization': 0.0001,
    'learning_rate': 0.00005,
    'early_stop_patience': 50
}

# Schedule settings
AUTO_START = "16:45"
