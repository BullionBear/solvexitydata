import os
import argparse
from sqlalchemy import create_engine
from datetime import datetime, timezone, timedelta
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

db_url = os.getenv("DB_URL")

def insert_kline_parser():
    parser = argparse.ArgumentParser(description="Insert an API key")
    parser.add_argument("--symbol", required=True, help="Symbol, e.g. BTCUSDT")
    parser.add_argument("--interval", required=True, help="Interval, e.g. 1m")
    parser.add_argument("--start_ts", type=int, required=True, help="Start timestamp in milliseconds (Unix time)")
    parser.add_argument("--end_ts", type=int, required=True, help="End timestamp in milliseconds (Unix time)")
    return parser

if __name__ == "__main__":
    parser = insert_kline_parser()
    args = parser.parse_args()
    c = Client()
    start_ts = args.start_ts
    end_ts = args.end_ts
    day_interval = 86400000  # One day in milliseconds
    num_days = (end_ts - start_ts) // day_interval + 1  # Include the end date

    columns = [
        "open_time", "open_px", "high_px", "low_px", "close_px", "base_asset_volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "unused_field"
    ]
    # Calculate the number of days to iterate
    engine = create_engine(db_url)
    current_ts = start_ts
    # Use tqdm to add a progress bar
    for i in tqdm(range(num_days), desc="Processing dates"):
        next_ts = min(current_ts + day_interval, end_ts)
        klines = c.get_historical_klines(args.symbol, args.interval, current_ts, next_ts - 1)
        df_kline = pd.DataFrame(klines, columns=columns)
        df_kline["symbol"] = args.symbol
        df_kline["interval"] = args.interval
        df_kline.drop(columns=["unused_field"], inplace=True)
        df_kline.to_sql("kline", con=engine, if_exists="append", index=False)
        current_ts = next_ts