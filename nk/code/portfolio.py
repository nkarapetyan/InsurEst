#############################################################
# Author: Nare Karapetyan                                   #
#                                                           #
# file: portfolio.py                                        #
# description:                                              #
#############################################################

import csv
from math import log
import numpy as np
from array import array
import math
import matplotlib.pyplot as plt

from sets import Set

def saveDataFrame(df, data, outFile):
    n_df = df.append(data)
    n_df.to_csv(outFile, index=False)
    return n_df


#print scatterplot
# x and y are the dataframe column names
# return the figure
def scatter_plot(data, x, y):
    f = plt.figure()
    ax = f.add_subplot(1, 1, 1)
    ax.scatter(data[x], data[y])
    plt.title(x + ' and ' + y + ' distribution')
    plt.xlabel(x)
    plt.ylabel(y)
    #plt.show()
    return f

#missing values function
def data_isNull(data):
    return sum(data.isnull())

#Define a generic function using Pandas replace function
def coding(col,codeList):
    colCoded = pd.Series(col, copy=True)
    for s in codeList:
        if(type(s) is str):
            colCoded.replace(key, codeList.index(s), inplace=True)
    return colCoded

new = [] 
def ccat(data):
    t_m = 'Driver_Total_Male'
    t_f = 'Driver_Total_Female'
    t_total = 'Driver_Total'
    t = data[t_m] + data[t_f]
    if( t != data[t_total]):
        s = 'Error'
    else:
        s = str(data[t_m]) + str(data[t_f])
    if s in new:
        print new.index(s)
    else:
        new.append(s)
        print new.index(s)
    return s

## col = 0 then the function is applied to each column
## if 1 then to the row
def apply_function(fn, data, col):
    return data.apply(fn, axis=col)


###-------------
#Using Pandas
###
def saveColumns(keep_cols, inFile, outFile):
    import pandas as pd
    f=pd.read_csv(inFile)
    new_f = f[keep_cols]
    new_f.to_csv(outFile, index=False)
    return new_f

###--------------------------------------------###
#Helper function for reading data from csv file
#--------------------------------------------
# \param file and i: name of file and number of column
# \return i-th column from the file
###--------------------------------------------###
def readCol(file, i):
    with open(file, 'rb') as csvfile:
        data = csv.reader(csvfile, delimiter=' ')
        col = [x[i] for x in data]
        return map(float,col[1:])


def readRow(file, i):
    with open(file, 'rb') as csvfile:
        data = csv.reader(csvfile, delimiter='\t')
        row = [x[i] for x in data]
        return map(float,row[1:])

def getHeader(file):
    with open(file, 'rb') as csvfile:
        data = csv.reader(csvfile, delimiter='\t')
        heading = data.next()
        csvfile.close()
        print "size of heading --> " 
        print len(heading)


###--------------------------------------------###
#Helper function for plotting the data
#--------------------------------------------
# \param file and i: name of file and number of column
# \return i-th column from the file
###--------------------------------------------###
def plotting(X, T):
    f = plt.figure()
    plt.plot(X, T, 'rx')
    plt.show()

    return  f

def saveInPdf(filename, figure):
    figure.savefig(filename)

