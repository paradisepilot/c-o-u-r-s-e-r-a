'''
(c) 2011, 2012 Georgia Tech Research Corporation
This source code is released under the New BSD license.  Please see
http://wiki.quantsoftware.org/index.php?title=QSTK_License
for license details.

Created on January, 24, 2013

@author: Sourabh Bajaj
@contact: sourabhbajaj@gatech.edu
@summary: Example tutorial code.
'''

# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

# other imoprts
import csv

print "Pandas Version", pd.__version__

def main():
    ''' Main Function'''

    # List of symbols
    # ls_symbols = ["AAPL", "GLD", "GOOG", "$SPX", "XOM"]
    #ls_symbols = ["AXP", "HPQ", "IBM", "$SPX", "HNZ"]
    #ls_symbols = ["C", "GS", "IBM", "$SPX", "HNZ"]
    ls_symbols = ['BRCM', 'ADBE', 'AMD', '$SPX', 'ADI']

    # Start and End date of the charts
    dt_start = dt.datetime(2010,  1,  1)
    dt_end   = dt.datetime(2010, 12, 31)

    # We need closing prices so the timestamp should be hours=16.
    dt_timeofday = dt.timedelta(hours=16)

    # Get a list of trading days between the start and the end.
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

    # Creating an object of the dataaccess class with Yahoo as the source.
    c_dataobj = da.DataAccess('Yahoo')

    # Keys to be read from the data, it is good to read everything in one go.
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    # Reading the data, now d_data is a dictionary with the keys above.
    # Timestamps and symbols are the ones that were specified before.
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    # Getting the numpy ndarray of close prices.
    na_price = d_data['close'].values
    print na_price

    with open('closing-prices.csv',"wb") as myCsvFile:
        myCsvWriter = csv.writer(myCsvFile,delimiter='\t')
        myCsvWriter.writerow(ls_symbols)
        for i in range(len(na_price)):
            myCsvWriter.writerow(na_price[i,:])
        myCsvFile.close()

if __name__ == '__main__':
    main()
