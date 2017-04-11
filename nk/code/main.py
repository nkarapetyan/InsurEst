#!/usr/bin/python

import getopt, sys
import numpy as np

from portfolio import *

def main(argv):
    #inputFile = ''
    #try:
     #   opts, args = getopt.getopt(argv, "i:", ["ifile="])
    #except getopt.GetoptError:
     #   print 'main.py -i <inputfile>'
      #  sys.exit()
    #for opt, arg in opts:
     #    if opt == '-i':
      #      inputFile = arg

    import pandas as pd
    #with open("../data/cols_part_3.csv") as f:
     #   keep_cols = f.read().splitlines()
    #print keep_cols
    outFile = "../data/data_part_3.csv"
    data_file_name = '../data/cleaned_training_data_2016_ver_02.csv'

    #1 to make a portion of data in new cvs by selected columns
    #saveColumns(keep_cols, inputFile, outFile)

    dataFrame = pd.read_csv(data_file_name)
    #0 print the number of the columns
    print len(dataFrame.index)

    #2 print apply_function(data_missing, dataFrame, 0)

    #3
    #for col_name in keep_cols:
        #test = dataFrame.groupby(col_name)
    #3.1 group variables in Python to calculate count, average, sum
    #print test.describe(include='all')
    #3.2 generate frequency tables
        #print test.size()

    #5 printing the scatterpolot
    col_y = 'Loss_Amount'
    #col_x = 'Driver_Total_Related_To_Insured_Child'
    #scatter_plot(dataFrame, col_x, col_y)
    for col in dataFrame:
        print col
        dataFrame[col] = coding(dataFrame[col])
        f = scatter_plot(dataFrame, col, col_y)
        image_name = col + '.png'
        f.savefig(image_name, bbox_inches = 'tight')

    #6 merging some columns
    t_m = 'Driver_Total_Male'
    t_f = 'Driver_Total_Female'
    t_pairs = 'Male_Female_pairs_numeric'
    #X = readCol('new.csv',0)
    #plotting(X, dataFrame[col_y])

    #7 concat two databases
    d2 = pd.read_csv("../data/data_changed.csv")
    d3 = pd.read_csv("new.csv")
    #dataFrame = saveDataFrame(dataFrame, d2, 'changed.csv')
    #saveDataFrame(dataFrame, d3, 'changed.csv')

    #new_df = apply_function(ccat, dataFrame, 1) # apply to rows
  #  df = pd.DataFrame() # new empty data frame for storing new values
 #   saveDataFrame(df, new_df, 'changed.csv')



    #field1 = "PolicyNo"
    #field2 = "Annual_Premium"
    #field3 = "Loss_Amount"
    #print dataFile.iloc[1] # to access the i-th row
    #print dataFile.name # to access column with name

    #dataFile.iloc[i].name # for accessng i-th row and column named name


    #header = getHeader(inputFile)
    #for el in header:
     #   print el + '\n'
    #X = readCol(inputFile,indexes[0])
    #T = readCol(inputFile,indexes[2])
    #plotting(X, T)

if __name__ == "__main__":
    main(sys.argv[1:])


