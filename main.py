import yfinance as yf
import pickle
import sys
import threading
# from p_s_class import Portfolio, Stock



class Portfolio():
    def __init__(self, name):
        self.name = name
        self.stocks_owned = []

    def get_stocks_owned(self):
        # todo make this return the actual tikr and quantity not the object
        for i in self.stocks_owned:
            print(i.tikr)

    def get_name(self):
        return self.name

    def add_stock(self, stock_tikr, stock_q):
        self.stocks_owned.append(Stock(stock_tikr, stock_q))

    def save_portfolio(self):
        with open("portfolio_" + str(self.get_name()), 'wb') as pickle_out:
            pickle.dump(self, pickle_out)

    def get_performance(self): # todo take current price and purchase price, calculate performance td
        for i in self.stocks_owned:
            current = i.get_price()
            print(current - i.purchase_price)

    def remove_stock(self, tikr):
        for x in self.stocks_owned:
            if x.tikr == tikr:
                self.stocks_owned.remove(x)
                print("removed")
            else:
                print("Wrong tikr")

class Stock():
    def __init__(self, tikr):
        self.tikr = tikr
        self.quant = quant
        self.purchase_price = purchase_price

    def get_info(self):
        print(self.data.get_info())
        self.data = yf.Ticker(self.tikr)

    def get_price(self):
        self.data = yf.Ticker(self.tikr)
        info = self.data.get_info()
        print(info['currentPrice'])

class Portfolio_Stock(Stock):
    def __init__(self, tikr, quant, purchase_price=0):
        self.tikr = tikr
        self.quant = quant
        self.purchase_price = purchase_price

def load_portfolio(name):
    with open('portfolio_' + name, "rb") as pickle_in:
        portfolio = pickle.load(pickle_in)
        return portfolio

mxct = Stock("mxct", 100)
mxct.get_price()


menuon = True
while menuon: #todo make this a true menu that can access the portfolios and methods
    print("")
    answer = input("What would you like to do?/n")
    if answer == "1":
        print("hi")
    elif answer == "2":
        print("Hello")
    elif answer == "3":
        print("hey")
    elif answer == "4":
        print("4")
    elif answer == "5":
        print("5")
    elif answer == "6":
        answer = None
    else:
        print("Invalid choice, try again")