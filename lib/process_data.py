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
    df = df.copy()
    df = df.fillna(0.0)
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.fillna(0.0)

    data_np = df.to_numpy()
    
    scaler = StandardScaler()
    data_nps = scaler.fit_transform(data_np)
    
    train, val = sklearn.model_selection.train_test_split(data_nps, test_size=0.05, shuffle=False)
    x_train = createWindows(train, windowSize)
    y_train = createLabels(train, windowSize, 0)
    x_val = createWindows(val, windowSize)
    y_val = createLabels(val, windowSize, 0)
    
    return x_train, y_train, x_val, y_val, scaler

def get_prediction_data(df, scaler, windowSize):
    df = df.copy()
    df = df.fillna(0.0)
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.fillna(0.0)

    latest_data = df.tail(windowSize+1)[:-1]
    scaled_data = scaler.transform(latest_data.to_numpy())
    
    return np.array([scaled_data])

