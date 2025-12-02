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

    # Set style
    sns.set_style(style)

    sns_plot = sns.lineplot(x="Date", y="Price", hue="Ticker", data=long_df)
    sns_plot.set_title("Stock Prices")
    sns_plot.set_xlabel("Date")
    sns_plot.set_ylabel("Price (USD)")
    sns_plot.legend(title="Ticker")

    # Show the plot
    plt.tight_layout()
    plt.show()