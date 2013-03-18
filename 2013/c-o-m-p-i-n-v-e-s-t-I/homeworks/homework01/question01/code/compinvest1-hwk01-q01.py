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
import numpy as np

print "Pandas Version", pd.__version__

####################################################################################################
def simulate(startDate, endDate, symbols, allocations, closingPrices):

    sharpeRatio = 0
    cumulativeReturn = 0

    temp1 = closingPrices.copy()
    temp2 = closingPrices.copy()
    temp1 = temp1[range(0,(len(temp1)-1)),:]
    temp2 = temp2[range(1,len(temp2)),:]

    dailyReturns = np.zeros(closingPrices.shape)
    dailyReturns[0,:] = np.ones(len(allocations))
    dailyReturns[range(1,closingPrices.shape[0]),:] = temp2 / temp1

    portfolio = np.zeros(closingPrices.shape)
    portfolio[0,:] = allocations
    for i in range(1,closingPrices.shape[0]):
        portfolio[i,:] = portfolio[i-1,] * dailyReturns[i,:]

    portfolioTotal = np.sum(portfolio, axis = 1)

    portfolioDailyReturns = np.zeros(len(portfolioTotal))
    portfolioDailyReturns[range(1,len(portfolioDailyReturns))] = -1 + portfolioTotal[range(1,len(portfolioTotal))] / portfolioTotal[range(0,len(portfolioTotal)-1)]

    stdDev = np.std(portfolioDailyReturns)
    avgDailyReturn = np.mean(portfolioDailyReturns)
    sharpeRatio = np.sqrt(closingPrices.shape[0]) * avgDailyReturn / stdDev
    cumulativeReturn = portfolioTotal[len(portfolioTotal)-1] / portfolioTotal[0]

    return stdDev, avgDailyReturn, sharpeRatio, cumulativeReturn

####################################################################################################
def main():
    ''' Main Function'''

    # List of symbols
    #ls_symbols = ["AAPL", "GLD", "GOOG", "$SPX", "XOM"]
    ls_symbols = ["AAPL", "GLD", "GOOG", "$SPX", "XOM"]

    # Start and End date of the charts
    dt_start = dt.datetime(2011,  1,  1)
    dt_end   = dt.datetime(2011, 12, 31)

    #myCsvFile = open('closing-prices-1.csv',"r")
    #myCsvFile = open('closing-prices-2.csv',"r")
    myCsvFile = open('closing-prices-4.csv',"r")
    myClosingPrices = np.genfromtxt(myCsvFile, skip_header = 0, delimiter='\t', dtype=None)
    myCsvFile.close()
    symbols = myClosingPrices[0,:]

    myCsvFile = open('closing-prices-4.csv',"r")
    myClosingPrices = np.genfromtxt(myCsvFile, skip_header = 1, delimiter='\t', dtype=float)
    myCsvFile.close()

    myCsvFile = open('portfolios.csv',"wb")
    myCsvWriter = csv.writer(myCsvFile,delimiter='\t')
    #myCsvWriter.writerow(['C', 'GS', 'IBM', 'HNZ', 'stdDev', 'avgDailyReturn', 'Sharpe', 'cumulativeReturn'])
    myCsvWriter.writerow([symbols, 'stdDev', 'avgDailyReturn', 'Sharpe', 'cumulativeReturn'])

    increments = np.array(range(0,11),dtype=float) / 10
    for i in increments:
        for j in increments:
            for k in increments:
                l = 1 - i - j - k
                #if (1e-10 < l):
                if (0 < l):
                    print i,j,k,l
                    myAllocations = np.array([i, j, k, 0.00, l])
                    myStdDev, myAvgDailyReturn, mySharpeRatio, myCumulativeReturn = simulate(
                        startDate = dt_start,
                        endDate = dt_end,
                        symbols = ls_symbols,
                        allocations = myAllocations,
                        closingPrices = myClosingPrices
                        )
                    myCsvWriter.writerow([i,j,k,l,myStdDev, myAvgDailyReturn, mySharpeRatio, myCumulativeReturn])

    myCsvFile.close()

    #myStdDev, myAvgDailyReturn, mySharpeRatio, myCumulativeReturn = simulate(
    #    startDate = dt_start,
    #    endDate = dt_end,
    #    symbols = ls_symbols,
    #    allocations = myAllocations,
    #    closingPrices = myClosingPrices
    #    )

    #print myStdDev
    #print myAvgDailyReturn
    #print mySharpeRatio
    #print myCumulativeReturn

####################################################################################################
####################################################################################################
if __name__ == '__main__':
    main()

