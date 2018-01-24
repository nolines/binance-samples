#!/usr/bin/env python
# coding=utf-8
import argparse
import operator
import threading

from binance.client import Client
from binance.config import *
from decimal import Decimal
from operator import itemgetter, attrgetter

client = Client(api_key, api_secret)

parser = argparse.ArgumentParser()
parser.add_argument("--symbol", type=str, help="Market Symbol (Ex: TRXBTC)")
parser.add_argument("--quantity", type=int, help="Buy/Sell Quantity", default=1)
parser.add_argument("--feepercentage", type=int, help="Check binance to see latest fees. https://www.binance.com/fees.html", default=0.005)

options = parser.parse_args()

symbol = options.symbol
quantity = options.quantity
fee_percentage = options.feepercentage
bnb_fee_percentage = 0.05

def main():
    # calculate_average_investment()
    # check_price()
    # get_account_info()
    get_account_info_symbol()
    # create_order('SELL')
    # create_order('BUY')

def create_order(orderType):
    print('Creating an order')
    try:
        if orderType is 'BUY':
            print('Order Type: ', orderType)        
            client.order_market_buy(
                 symbol=symbol,
                 quantity=quantity)
        elif orderType is 'SELL':
            print('Order Type: ', orderType)
            client.order_market_sell(
                             symbol=symbol,
                             quantity=quantity)
    except Exception as e:
        print (e)
        return None        

# def check_fee():
    # if hasEnoughBNB:
    #     calculate_with_bnb()
    # else:
    #     calculate_fee_with_bnb()

# def check_present_bnb():
#     current_info = client.get_exchange_info(symbol="BNBBTC")
#     return current_info.price * 0.005

# def get_account_info():
#     account_info = client.get_account()
#     print(account_info)
#     for i in range(len(account_info['balances'])):
#         if account_info['balances'][i]['asset'] is 'BNB':
#             print(account_info['balances'][i]['free'])

def get_account_info_symbol():
    account_info = client.get_account()
    for i in range(len(account_info['balances'])):
        if account_info['balances'][i]['asset'] == symbol:
            print(account_info['balances'][i]['free'])
    
    user_input = input('Do you want to clean dust of ' +  symbol + ' (YES/NO):')
    sell_symbol = symbol + 'BNB'

    print(user_input)
    if user_input == 'YES':
        print("Creating order for ", sell_symbol)
        client.order_market_sell(
                             symbol=sell_symbol,
                             quantity=account_info['balances'][i]['free'])
    elif user_input == 'NO':
        print("Exit!")
        

# def get_my_trades():
#     histrorical_trades = client.get_my_trades(symbol=symbol)
#     return histrorical_trades

# def calculate_average_investment():
#     trades = get_my_trades()
#     buys = 0
#     sells = 0
#     total = 0
    # for i in range(len(trades)):
    #     if trades[i]['isBuyer']:
    #         print("qty:", trades[i]['qty'])
    #         print("price:", trades[i]['price'])
    #         total += Decimal(trades[i]['qty'])
    #         buys += Decimal(trades[i]['price']) * Decimal(trades[i]['qty'])
    #     elif not trades[i]['isBuyer']:
    #         print("-qty:", trades[i]['qty'])
    #         print("-price:", trades[i]['price'])
    #         total -= Decimal(trades[i]['qty'])
    #         sells += Decimal(trades[i]['price']) * Decimal(trades[i]['qty'])
    # print('Buys:', buys)
    # print('Sells:', sells)

    # result = (buys - sells) / total
    # print(result)

# def check_price():
#     threading.Timer(5.0, check_price).start()
#     current_price = client.get_ticker(symbol=symbol)
#     print("Price: ", current_price)

main()
