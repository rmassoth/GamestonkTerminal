""" Yahoo Finance View """
__docformat__ = "numpy"

import os
from tabulate import tabulate
from gamestonk_terminal.helper_funcs import export_data
from gamestonk_terminal.stocks.discovery import yahoofinance_model


def display_gainers(num_stocks: int, export: str):
    """Display gainers. [Source: Yahoo Finance]

    Parameters
    ----------
    num_stocks: int
        Number of stocks to display
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    df_gainers = yahoofinance_model.get_gainers()
    df_gainers.dropna(how="all", axis=1, inplace=True)
    df_gainers = df_gainers.replace(float("NaN"), "")

    if df_gainers.empty:
        print("No gainers found.")
    else:
        print(
            tabulate(
                df_gainers.head(num_stocks),
                headers=df_gainers.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
    print("")

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "gainers",
        df_gainers,
    )


def display_losers(num_stocks: int, export: str):
    """Display losers. [Source: Yahoo Finance]

    Parameters
    ----------
    num_stocks: int
        Number of stocks to display
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    df_losers = yahoofinance_model.get_losers()
    df_losers.dropna(how="all", axis=1, inplace=True)
    df_losers = df_losers.replace(float("NaN"), "")

    if df_losers.empty:
        print("No losers found.")
    else:
        print(
            tabulate(
                df_losers.head(num_stocks),
                headers=df_losers.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
    print("")

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "losers",
        df_losers,
    )


def display_undervalued(num_stocks: int, export: str):
    """Display most undervalued growth stock. [Source: Yahoo Finance]

    Parameters
    ----------
    num_stocks: int
        Number of stocks to display
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    df = yahoofinance_model.get_undervalued()
    df.dropna(how="all", axis=1, inplace=True)
    df = df.replace(float("NaN"), "")

    if df.empty:
        print("No data found.")
    else:
        print(
            tabulate(
                df.head(num_stocks),
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
    print("")

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "undervalued",
        df,
    )
