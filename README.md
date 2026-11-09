# GoldData

XAUUSD price history exported from MetaTrader 5 for backtesting the gold bots.

## Layout
```
<broker server>_XAUUSD/
  _INFO.txt          contract size, point, digits, candle counts
  M1/ M3/ M5/ M15/ M30/ H1/ H4/ D1/
    XAUUSD_<TF>_<YEAR>.csv
```
Columns: `time,datetime_server,open,high,low,close,tick_volume,spread`

- `time` = broker **server time** as epoch seconds (IC Markets: GMT+2 winter / GMT+3 summer, NY-close aligned). Singapore time = UTC+8.
- `spread` is in points (gold: 1 point = $0.01). This account is IC Markets **Raw**: tight spread (median ~5 points) but commission per lot. Use that in backtests.
- Contract size 100 → 0.01 lot = $1 per $1 gold move.

## Load
```python
from load_data import load
rates = load("M5", 2024, 2026)   # same fields as mt5.copy_rates_range
```

## Update
Run `Download_Backtest_Data.bat` on the laptop (MT5 open), then upload the refreshed folder here.
Past years don't change; only the current year's files need replacing.
