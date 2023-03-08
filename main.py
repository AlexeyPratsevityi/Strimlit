import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf


st.write("""
#  Японская свечная диаграма для Apple Inc. Цена на акции c 30. 01 2022.
(идея  нагло украдена у https://github.com/danchenkoEgor)
""")

tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1m',interval='1mo', start='2022-01-30')
tickerDf = tickerDf[['Open', 'High', 'Low', 'Close', 'Volume']]
fig, ax = mpf.plot(tickerDf, type='candle', volume=True, returnfig=True)
st.pyplot(fig)






