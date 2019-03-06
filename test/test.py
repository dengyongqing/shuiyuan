# -*-coding:utf-8 -*-
import os
import yahoo_finance as yf
from yahoo_finance import Currency

def test():
     eur_pln = Currency('EURPLN')
     print(eur_pln.get_rate())


test()