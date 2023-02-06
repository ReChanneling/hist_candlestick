import requests
import json
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from utils.util import interval_to_minutes

class History:
    URL: str = "https://api.binance.com/api/v3/klines"
    limit = '1000'
    
    symbol: str
    interval: str
    candle_number: int
    end_time: int
    start_time: int
    df = None
    
    def __init__(self, symbol = "BTCUSDT", interval = "1m", candle_number = 120) -> None:  
        self.symbol = symbol
        self.interval = interval
        self.candle_number = candle_number
        self.endTime = int(dt.datetime.now().timestamp() * 1000)
        self.startTime = int((dt.datetime.now() - dt.timedelta(minutes = interval_to_minutes(self.interval) * self.candle_number)).timestamp() * 1000)
        self.update_df()

    def update_df(self) -> None:
        req_params = {
            "symbol": self.symbol, 
            "interval": self.interval, 
            "startTime": str(self.startTime), 
            "endTime": str(self.endTime), 
            "limit": self.limit
        }
        #       x       x       x       x               x
        #date   open    high    low     close   volume  date_close  qav     not     tbbav   tbqav   ignorable
        self.df = pd.DataFrame(json.loads(requests.get(self.URL, params=req_params).text))
        self.df = self.df.iloc[:, 0:5]
        self.df.columns = ['date', 'open', 'high', 'low', 'close']
        
        self.df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in self.df.date]
    
if __name__ == '__main__':
    history = History()
    print(history.df)
        