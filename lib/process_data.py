from sklearn.preprocessing import StandardScaler
import sklearn
import numpy as np
import pandas as pd

def createWindows(data, windowSize):
    dataset = []
    i = 0
    while i + windowSize < len(data):  
        window = data[i:i+windowSize]
        dataset.append(window)
        i += (windowSize + 1)
        
    return np.array(dataset)

def createLabels(data, windowSize, labelColumn):
    labels = []
    i = 0
    while i + windowSize < len(data):
        label = data[i + windowSize, labelColumn]
        labels.append(label)
        i += (windowSize + 1)

    return np.array(labels)

def process_data(df, windowSize=5):
    try:
        if df is None or df.empty:
            raise ValueError("Input dataframe is None or empty")
        
        if len(df) <= windowSize:
            raise ValueError(f"Not enough data points ({len(df)}) for window size {windowSize}")

        df = df.copy()
        
        # Handle missing values
        df = df.fillna(0.0)
        df = df.apply(pd.to_numeric, errors='coerce')
        df = df.fillna(0.0)
        
        if df.isnull().any().any():
            raise ValueError("Data contains null values after preprocessing")

        data_np = df.to_numpy()
        
        scaler = StandardScaler()
        data_nps = scaler.fit_transform(data_np)
        
        if len(data_nps) <= windowSize:
            raise ValueError(f"Not enough scaled data points ({len(data_nps)}) for window size {windowSize}")
        
        # Split data into training and validation sets
        train, val = sklearn.model_selection.train_test_split(data_nps, test_size=0.05, shuffle=False)
        
        x_train = createWindows(train, windowSize)
        y_train = createLabels(train, windowSize, 0)
        x_val = createWindows(val, windowSize)
        y_val = createLabels(val, windowSize, 0)
        
        if len(x_train) == 0 or len(y_train) == 0 or len(x_val) == 0 or len(y_val) == 0:
            raise ValueError("One or more of the training/validation sets is empty")
        
        return x_train, y_train, x_val, y_val, scaler
    
    except Exception as e:
        print(f"Error in process_data: {e}")
        raise

def get_prediction_data(df, scaler, windowSize):
    try:
        if df is None or df.empty:
            raise ValueError("Input dataframe is None or empty")
            
        if scaler is None:
            raise ValueError("Scaler object is None")
            
        if len(df) <= windowSize:
            raise ValueError(f"Not enough data points ({len(df)}) for window size {windowSize}")

        df = df.copy()
        
        # Handle missing values
        df = df.fillna(0.0)
        df = df.apply(pd.to_numeric, errors='coerce')
        df = df.fillna(0.0)
        
        if df.isnull().any().any():
            raise ValueError("Data contains null values after preprocessing")

        latest_data = df.tail(windowSize+1)[:-1]
        if len(latest_data) != windowSize:
            raise ValueError(f"Could not get enough latest data points (got {len(latest_data)}, need {windowSize})")
            
        scaled_data = scaler.transform(latest_data.to_numpy())
        
        return np.array([scaled_data])
    
    except Exception as e:
        print(f"Error in get_prediction_data: {e}")
        raise

