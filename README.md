# Stock Price Predictor

⚠️ **DISCLAIMER**

This software is for educational and research purposes only. It:
- Is NOT financial advice
- Should NOT be used for actual trading decisions
- Makes NO guarantees about prediction accuracy
- Does NOT guarantee any financial returns
- May contain errors or inaccuracies

Past performance does not guarantee future results. Always consult with a qualified financial advisor before making any investment decisions. The creators and contributors of this software are not responsible for any financial losses incurred from using this tool.

## Overview

A machine learning model that predicts stock prices using historical data and economic indicators. The model uses a neural network to analyze patterns in stock prices along with various economic indicators from different countries.

## Features

- Downloads and processes stock data using Yahoo Finance API
- Collects economic indicators (CPI, GDP, Interest Rates) from World Bank API
- Calculates Dynamic Moving Averages (DMA) for technical analysis
- Uses a deep neural network for price prediction
- Supports GPU acceleration (optional)

## Prerequisites

- Python 3.12 or higher
- pip (Python package installer)
- Internet connection for data downloads

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Stock-Predictor-Prototype-v2.git
cd Stock-Predictor-Prototype-v2
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# On Linux/Mac:
source env/bin/activate
# On Windows:
# env\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

Edit `config.py` to customize the model:

- `TICKERS`: List of stock tickers to analyze (default: ['^FTLC'])
- `COUNTRIES`: List of countries for economic indicators
- `WINDOW_SIZE`: Number of days to use for prediction (default: 5)
- `EPOCHS`: Number of training epochs (default: 500)
- `USE_GPU`: Set to True to enable GPU acceleration if available

## Usage

Run the predictor:
```bash
python main.py
```

The program will:
1. Download stock and economic data
2. Process and prepare the data
3. Train the neural network
4. Output the predicted stock price for tomorrow

## Model Architecture

The neural network consists of:
- Multiple dense layers with ReLU activation
- Early stopping to prevent overfitting
- Configurable learning rate and network structure
- Optional GPU support for faster training

## Project Structure

```
├── config.py           # Configuration settings
├── main.py            # Main entry point
├── requirements.txt   # Package dependencies
└── lib/              # Core library code
    ├── __init__.py
    ├── build_db.py           # Database construction
    ├── fetch_data.py         # Data retrieval
    ├── get_data_functions.py # Economic data collection
    ├── get_ticker_data.py    # Stock data collection
    ├── NN.py                 # Neural network model
    └── process_data.py       # Data processing
```

## Troubleshooting

- If you encounter GPU-related errors, ensure you have CUDA installed or set `USE_GPU = False` in config.py
- For database errors, check if SQLite3 is properly installed
- For data download issues, verify your internet connection and API access

## License

[Your License Here]

## Contributing

Feel free to submit issues and pull requests.

## Acknowledgments

- Yahoo Finance for stock data
- World Bank for economic indicators
- TensorFlow team for the deep learning framework