from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
import datetime as dt

def setTimeFrame(__timeframe = "hour"):
    if __timeframe.lower() == "hour":
        tf = TimeFrame.Hour
    elif __timeframe.lower() == "day":
        tf = TimeFrame.Day
    elif __timeframe.lower() == "minute":
        tf = TimeFrame.Minute
    elif __timeframe.lower() == "week":
        tf = TimeFrame.Week
    else:
        raise ValueError("Unaccounted for timeframe. Please select from ['minute','hour','day','week']")
    return tf

def get_crypto_data(symbols, start, end, timeframe:str, date_format =r"%Y-%m-%d" ):
    # No keys required for crypto data
    client = CryptoHistoricalDataClient()

    timeframe = setTimeFrame(timeframe)

    # Creating request object
    request_params = CryptoBarsRequest(
                        symbol_or_symbols=symbols,
                        timeframe=timeframe,
                        start=dt.datetime.strptime(start,date_format),
                        end=dt.datetime.strptime(end,date_format)
                        )
    # Retrieve daily bars for Bitcoin in a DataFrame
    crypto_bars = client.get_crypto_bars(request_params)
    # Convert to dataframe
    df = crypto_bars.df
    return df
