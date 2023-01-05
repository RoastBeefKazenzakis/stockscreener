import screener
import finpie
import pandas
import time
import sqlite3
import nasdaqdatalink

# set api key
nasdaqdatalink.read_key(filename="D:/Projects/Python/StockScreener/stockscreener/nasdaq_api_key.txt")

# get marketcap for each symbol
def screenStockMCAP(ticker):
    fd = finpie.Fundamentals(ticker)
    print('Looking for market cap for ' + str(ticker) + '...')
    screenedValue = int(fd.key_metrics().market_cap)
    return screenedValue

#init db connection

conn = sqlite3.connect("stocks.db")
cur = conn.cursor()

# create table
cur.execute("CREATE TABLE IF NOT EXISTS stocks (symbol TEXT, marketcap INTEGER)")

res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchall())

res = cur.execute("SELECT * FROM stocks")
print(res.fetchall())


# list all symbols
tickers = finpie.nasdaq_tickers()

# push each symbol to db
for stock in tickers['Symbol']:
    cur.execute("INSERT INTO stocks VALUES (?, ?)", (stock, screenStockMCAP(stock)))
    time.sleep(0.33)
