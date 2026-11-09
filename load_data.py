"""Load GoldData CSVs.   from load_data import load
rates = load("M5", 2024, 2026)            # numpy structured array, MT5 field names
rates = load("M1", 2025, broker="ICMarketsSC-Demo_XAUUSD")
"""
import os, glob
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DTYPE = [("time", "i8"), ("open", "f8"), ("high", "f8"), ("low", "f8"),
         ("close", "f8"), ("tick_volume", "i8"), ("spread", "i4")]


def load(tf="M5", year_from=None, year_to=None, broker="ICMarketsSC-Demo_XAUUSD"):
    files = sorted(glob.glob(os.path.join(HERE, broker, tf, f"*_{tf}_*.csv")))
    if year_to is None:
        year_to = year_from
    out = []
    for f in files:
        y = int(f.rsplit("_", 1)[1][:4])
        if (year_from and y < year_from) or (year_to and y > year_to):
            continue
        a = np.genfromtxt(f, delimiter=",", skip_header=1, usecols=(0, 2, 3, 4, 5, 6, 7))
        r = np.zeros(len(a), dtype=DTYPE)
        for i, (n, _) in enumerate(DTYPE):
            r[n] = a[:, i]
        out.append(r)
    if not out:
        raise FileNotFoundError(f"No {tf} files for {broker}")
    return np.concatenate(out)
