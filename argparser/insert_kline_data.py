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
    parser.add_argument("--start_date", required=True, help="YYYY-MM-DD (Inclusive)")
    parser.add_argument("--end_date", required=True, help="YYYY-MM-DD (Inclusive)")
    return parser

if __name__ == "__main__":
    parser = insert_kline_parser()
    args = parser.parse_args()
    c = Client()
    start_utc = datetime.strptime(args.start_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    end_utc = datetime.strptime(args.end_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    columns = [
        "open_time", "open", "high", "low", "close", "base_asset_volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "unused_field"
    ]
    # Calculate the number of days to iterate
    num_days = (end_utc - start_utc).days + 1  # Include the end date
    engine = create_engine(db_url)
    # Use tqdm to add a progress bar
    for i in tqdm(range(num_days), desc="Processing dates"):
        current_date = start_utc + timedelta(days=i)
        start_ts = int(current_date.timestamp() * 1000)
        end_ts = int((current_date + timedelta(days=1)).timestamp() * 1000) - 1
        klines = c.get_historical_klines(args.symbol, args.interval, start_ts, end_ts)
        df_kline = pd.DataFrame(klines, columns=columns)
        df_kline["symbol"] = args.symbol
        df_kline["interval"] = args.interval
        df_kline.drop(columns=["unused_field"], inplace=True)
        df_kline.to_sql("kline", con=engine, if_exists="append", index=False)