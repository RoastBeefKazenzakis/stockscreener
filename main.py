import screener
import finpie
import pandas

# list all symbols
tickers = finpie.nasdaq_tickers()
#print(tickers)
# now that we have all symbols, what will we do with them?
# have to decide on initial criteria to screen on.
def screenStock(ticker, criterion):
    fd = finpie.Fundamentals(ticker)
    print('Looking for ' + criterion + ' in ' + ticker + '...')
    screenedValue = str(fd.profile())
    print("Found " + criterion + " of " + screenedValue)

#stock = input("Enter a stock symbol for more information: ")

for stock in tickers['Symbol']:
    screenStock(stock, "profile")
    #print(stock)

#screener.printStockFinpie()
