import yfinance as yf

def fetch_data(tickers="AAPL", period="6mo"):
    data = yf.download(tickers, period=period)["Close"].reset_index()
    print(data)

    return data
