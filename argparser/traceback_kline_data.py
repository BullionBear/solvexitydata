import os
from sqlalchemy import create_engine
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv
from binance.client import Client
import datetime
import time

load_dotenv()

db_url = os.getenv("DB_URL")
"""
INSERT_LIST = {
    "BTCUSDT": 2020,
    "ETHUSDT": 2020,
    "ADAUSDT": 2020,
    "UNIUSDT": 2021,
    "XRPUSDT": 2020,
    "BNBUSDT": 2020,
    "DOGEUSDT": 2021,
    "SOLUSDT": 2021,
    "NEARUSDT": 2021,
    "IMXUSDT": 2022,
}
"""
INSERT_LIST = {
    "BTCUSDT": 2022,
    "ETHUSDT": 2022,
    "ADAUSDT": 2022,
    "UNIUSDT": 2022,
    "XRPUSDT": 2022,
    "BNBUSDT": 2022,
    "DOGEUSDT": 2022,
    "SOLUSDT": 2022,
    "NEARUSDT": 2022,
    "IMXUSDT": 2022,
}

HOUR_MS = 3600_000
END_TS = int(datetime.datetime.now().timestamp() * 1000) // HOUR_MS * HOUR_MS

def insert_kline(symbol: str):
    c = Client()
    
    start_dt = datetime.datetime(INSERT_LIST[symbol], 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
    start_ts = int(start_dt.timestamp() * 1000)
    end_ts = END_TS
    columns = [
        "open_time", "open_px", "high_px", "low_px", "close_px", "base_asset_volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "unused_field"
    ]
    interval = "1m"
    engine = create_engine(db_url)
    for i_start_ts in tqdm(range(start_ts, end_ts, HOUR_MS)):
        i_end_ts = i_start_ts + HOUR_MS
        klines = c.get_historical_klines(symbol, interval, i_start_ts, i_end_ts-1)
        df = pd.DataFrame(klines, columns=columns)
        df.drop(columns=["unused_field"], inplace=True)
        df["symbol"] = symbol
        df["interval"] = interval
        df.to_sql("kline", con=engine, if_exists="append", index=False)
        time.sleep(0.01)


if __name__ == "__main__":
    for symbol in INSERT_LIST:
        print(f"Inserting {symbol}...")
        insert_kline(symbol)

