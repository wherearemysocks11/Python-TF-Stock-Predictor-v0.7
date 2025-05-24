from sklearn.preprocessing import StandardScaler
import sklearn
import numpy as np
import pandas as pd
import tensorflow as tf

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

def process_data(df):
    df = df.fillna(0.0)
    df = df.astype(float)
    data_np = (pd.DataFrame(df)).to_numpy()
    standard_scaler = StandardScaler()
    data_nps = np.array(standard_scaler.fit_transform(data_np))
    train, test = sklearn.model_selection.train_test_split(data_nps, test_size=0.2, shuffle=False)
    val, test = sklearn.model_selection.train_test_split(test, test_size=0.5, shuffle=False)
    x_train = createWindows(train, 5)
    y_train = createLabels(train, 5, 0)
    x_val = createWindows(val, 5)
    y_val = createLabels(val, 5, 0)
    x_test = createWindows(test, 5)
    y_test = createLabels(test, 5, 0)
    return x_train, y_train, x_val, y_val, x_test, y_test


    
