#By Anugrah Noer Hadi
#This script is created in order to fill NaN value to certain time that is not recorded


import pandas as pd
import numpy as np
from datetime import datetime as dt
from datetime import timedelta

#write the datetime parser because the data contain date and time
dateparser=(lambda x: dt.strptime(x,"%Y%m%d %H:%M"))
#Read data with this term
#1. The second rows us pointless so skip it
#2. Using the first column as index
#3. Convert the first column with the name "--Timestamp---" that set as index to datetimeform

data=pd.read_table('coba.txt',skiprows=[1],index_col=0, parse_dates=['--Timestamp---'], date_parser=dateparser)

#create the complete datetime
year=data.index[0].year
month=data.index[0].month
day=data.index[0].day

start=dt(year,month,day,0,0,0)
end=dt(year,month,day,23,55,0)
cmpltdate=[start]
interval=timedelta(minutes=5)
while (start<end):
    start=start+interval
    cmpltdate.append(start)

#Fill the unrecorded data with nan
datacomplete=data.reindex(cmpltdate)

datacomplete.to_csv('coba-complete.csv',na_rep='NaN')