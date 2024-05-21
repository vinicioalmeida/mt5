import MetaTrader5 as mt5

mt5.initialize()
 
print(mt5.terminal_info())
print(mt5.version())

symbol="INDM24"
mt5.symbol_select(symbol,True)

lot = 10
price = mt5.symbol_info_tick(symbol).ask
deviation = 2
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": float(lot),
    "type": mt5.ORDER_TYPE_BUY,
    "price": price,
    "deviation": deviation,
    "magic": 123,
    "comment": "compra",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN
}
result = mt5.order_send(request)
print(result)
print(price)

mt5.shutdown()