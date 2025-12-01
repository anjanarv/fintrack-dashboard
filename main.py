from src.data_fetcher import fetch_data
from src.plotter import plot_data
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    tickers_str = os.getenv("TICKERS", "AAPL")  # default to AAPL if not set
    tickers = [t.strip() for t in tickers_str.split(",")]
     
    period = os.getenv("PERIOD", "6mo")  # dynamic period from env

    style = os.getenv("STYLE", "whitegrid") # dynamic style from env

    # Fetch stock data
    data = fetch_data(tickers, period)

    # Plot stock prices
    plot_data(data, style)

if __name__ == "__main__":
    main()
