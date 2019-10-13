# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si

# get live price of Apple
now=si.get_live_price("aapl")

# get quote table back as a data frame
quote = si.get_quote_table("aapl", dict_result = False)
