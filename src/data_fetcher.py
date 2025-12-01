import yfinance as yf

def fetch_data(tickers=None, period="6mo"):
    """
    Fetch closing price data for given tickers.
    Defaults to Apple (AAPL) if none provided.
    """
    if tickers is None:
        tickers = ["AAPL"]  # default ticker

    data = yf.download(tickers, period=period)["Close"].reset_index()
    print(data)

    return data
