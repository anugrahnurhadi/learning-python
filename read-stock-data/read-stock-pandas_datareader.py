import pandas as pd
from datetime import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt

data_source = 'yahoo'
start='2017-01-01'
end = '2018-01-01'

tickers = ['AAPL']
result = web.DataReader(tickers, data_source, start, end)
result.Close.plot()
plt.show()