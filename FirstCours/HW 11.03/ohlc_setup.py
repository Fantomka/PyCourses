"""
This file is using for read csv files with trades and
it produce an ohlc.csv files
valid time of trades: 7:00-3:00
input file: file.csv
output ohlc_5min.csv, ohlc_30min.csv, ohlc_240min.csv
"""

import csv
import datetime


def csv_reader(file):
    """
    Read a csv file
    """
    res = []
    reader = csv.reader(file)
    for row in reader:
        res.append(row)
    return res


def get_tickers(trades_list):
    return set(trades_list[:][0])


def trades_in_time(min, trades_list):
    begin_time = datetime.time(7, 0, 0, 0)
    end_time = datetime.time(23, 59, 59, 999999)
    with open('testfile.csv', 'w') as test:
        for line in trades_list:
            trade_time = datetime.time(int(line[3][11:13]), int(line[3][14:16]), int(line[3][17:19]), int(line[3][20:]))



csv_path = './Input/trades.csv'
with open(csv_path, 'r') as f_obj:
    trades = csv_reader(f_obj)
#trades_in_time(5, trades)
print(get_tickers(trades))