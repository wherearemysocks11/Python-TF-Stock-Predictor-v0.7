from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

def createWindows(data, windowSize):
    dataset = []
    i = 0
    while i + windowSize <= len(data):  
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

def process_data(df):
    df = df.fillna(0.0)
    df = df.astype(float)
    data_np = (pd.DataFrame(df)).to_numpy()
    scaler = StandardScaler()
    data_nps = scaler.fit_transform(data_np)
    windows = createWindows(data_nps, 5)
    labels = createLabels(data_nps, 5, 0)
    return windows, labels
