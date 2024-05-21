import sys
import MetaTrader5 as mt5
import time

mt5.initialize()
mt5.symbol_select('INDM24',True)

while(True):
    ativo = mt5.symbol_info_tick('INDM24')
    sys.stdout.write('\r' + str(ativo.last)) # \r apaga a cotação anterior
    sys.stdout.flush() # limpar a memória
    time.sleep(1)

mt5.shutdown()  
