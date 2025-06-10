import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def plot_training_history(history):
    """Plot training and validation metrics."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Plot loss
    ax1.plot(history.history['loss'], label='Training Loss')
    ax1.plot(history.history['val_loss'], label='Validation Loss')
    ax1.set_title('Model Loss')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss')
    ax1.legend()
    
    # Plot MAE
    ax2.plot(history.history['mae'], label='Training MAE')
    ax2.plot(history.history['val_mae'], label='Validation MAE')
    ax2.set_title('Model Mean Absolute Error')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('MAE')
    ax2.legend()
    
    plt.tight_layout()
    return fig

def plot_price_prediction(actual_prices, predicted_prices, dates, title="FTSE Price Prediction"):
    """Plot actual vs predicted prices."""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(dates, actual_prices, label='Actual', color='blue', alpha=0.7)
    ax.plot(dates, predicted_prices, label='Predicted', color='red', alpha=0.7)
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def plot_moving_averages(data, dma_periods, title="FTSE Moving Averages"):
    """Plot price with moving averages."""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data.index, data['close'], label='Close Price', color='blue', alpha=0.7)
    
    colors = ['red', 'green', 'orange', 'purple', 'brown']
    for period, color in zip(dma_periods, colors):
        ax.plot(data.index, data[f'dma_{period}'], 
                label=f'{period}-day MA', 
                color=color, 
                alpha=0.7)
    
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def plot_feature_correlations(df, title="Feature Correlations"):
    """Plot correlation matrix of features."""
    # Select numeric columns and compute correlation
    numeric_df = df.select_dtypes(include=[np.number])
    corr = numeric_df.corr()
    
    # Create correlation heatmap
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, ax=ax)
    ax.set_title(title)
    plt.tight_layout()
    return fig

def plot_feature_importance(model, feature_names):
    """Plot feature importance based on model weights."""
    # Get weights from the first dense layer
    weights = model.model.layers[1].get_weights()[0]
    importance = np.abs(weights).mean(axis=1)
    
    # Create feature importance plot
    fig, ax = plt.subplots(figsize=(10, 6))
    importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importance})
    importance_df = importance_df.sort_values('Importance', ascending=True)
    
    sns.barplot(data=importance_df, y='Feature', x='Importance', ax=ax)
    ax.set_title('Feature Importance')
    plt.tight_layout()
    return fig

def save_plots(figs, base_path='plots'):
    """Save all plots to files."""
    import os
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    for name, fig in figs.items():
        fig.savefig(os.path.join(base_path, f'{name}.png'))
        plt.close(fig)