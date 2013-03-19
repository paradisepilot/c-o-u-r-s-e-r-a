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
def simulate(allocations, closingPrices):

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

    myCsvFile = open('closing-prices.csv',"r")
    symbols = myCsvFile.readline().strip().split('\t')
    myCsvFile.close()

    myCsvFile = open('closing-prices.csv',"r")
    myClosingPrices = np.genfromtxt(myCsvFile, skip_header = 1, delimiter='\t', dtype=float)
    myCsvFile.close()

    myCsvFile = open('portfolios.csv',"wb")
    myCsvWriter = csv.writer(myCsvFile,delimiter='\t')
    myCsvWriter.writerow(symbols + ['stdDev', 'avgDailyReturn', 'Sharpe', 'cumulativeReturn'])

    for i in range(0,11):
        for j in range(0,11-i):
            for k in range(0,11-i-j):
                l = 10 - (i + j + k)
                if (-0.001 <= l):
                    #if (0.001 > l):
                    #    l = 0
                    print i,j,k,l
                    myAllocations = np.array([i/10.0, j/10.0, k/10.0, l/10.0])
                    myStdDev, myAvgDailyReturn, mySharpeRatio, myCumulativeReturn = simulate(
                        allocations   = myAllocations,
                        closingPrices = myClosingPrices
                        )
                    myCsvWriter.writerow([i/10.0,j/10.0,k/10.0,l/10.0,myStdDev, myAvgDailyReturn, mySharpeRatio, myCumulativeReturn])

    myCsvFile.close()

####################################################################################################
####################################################################################################
if __name__ == '__main__':
    main()

