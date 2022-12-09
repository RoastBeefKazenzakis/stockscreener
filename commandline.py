import cmd, sys

class StockScreeener(cmd.Cmd):
    intro = "Welcome to the Robinson Stock Screener, where your money turns into red lines and brokerage fees overnight. Type help to list commands, or input a ticker symbol.\n"
    prompt = "(rss) "
    file = None
    