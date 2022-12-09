#    List of internal functions
# readConfig: Get config from config file
# 
# 
# 
#     List of stock functions
# printStock: basic printout
# printStockFinancials: print the financials
# valueStockDFCF: Perform a discounted free cashflow on the given stock
# valueStockMultiple: Get the Forward P/E on the given stock



from pandas_datareader import nasdaq_trader as nt
import finpie as fp

def printStock():
    var = input("Enter a stock symbol for more information: ")
    print("Printing information for ", var)
    symbols = nt.get_nasdaq_symbols()
    stock = symbols.loc[var]
    print(stock)

def printStockFinancials():
    var = input("Enter a stock symbol for more information: ")
    symbols = nt.get_nasdaq_symbols()
    stock = symbols.loc[var]

def valueStockDFCF(stock):
    print(stock)