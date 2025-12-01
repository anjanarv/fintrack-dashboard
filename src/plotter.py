import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_data(data, style="whitegrid"):
     # unify multiple ticker columns
    long_df = pd.melt(
        data,
        id_vars=["Date"],          # keep Date as identifier
        value_vars=["AAPL", "AMZN", "GOOG", "MSFT"],  # tickers
        var_name="Ticker",         # new column for ticker name
        value_name="Price"         # new column for price
    )

    # Plot
    sns.set_style(style)
    plt.figure(figsize=(12,6))
    sns.lineplot(x="Date", y="Price", hue="Ticker", data=long_df)

    plt.title("Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend(title="Ticker")
    plt.show()
