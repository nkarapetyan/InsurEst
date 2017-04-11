####################################################
#
#  0.0. useful imports and variable declarations
#
####################################################
#NOTE: data_dir, path and col_types_file are the ones that should be defined
# with test_data_dir, and outfile
import csv
from math import log
import numpy as np
from array import array
import pandas as pd
import math
import matplotlib.pyplot as plt

from cleaner_functions import *

import ntpath # for extracting the filename

import glob # for processing all the

policy_ID = 'PolicyNo' # name of the first column for identifying the policies

data_dir = '../../data/'
complete_raw_train_data_file = 'training_data_2016.csv'
data_frame_file = complete_raw_train_data_file
path = data_dir + data_frame_file

col_types_file = "col_types.csv"

col_types = pd.read_csv(data_dir + col_types_file)

__1debug__ = False
if __1debug__:
    print col_types
    col_types_heading = col_types.columns.values
    print col_types_heading


test_data_dir =  data_dir + 'test/' #'test_portfolios/'
outfile = data_dir + 'cleaned_test_portfolios/'

before_cl_df = pd.DataFrame()
after_cl_df = pd.DataFrame()
print test_data_dir
i = 0

## iterating over all .csv files  in test_data_dir
for curr_file in glob.glob(test_data_dir + "*.csv"):
    i+=1
    print i

    print curr_file + " is processing ... \n"

    if __debug__:
        b_df = pd.read_csv(curr_file)
        frames = [b_df, before_cl_df]
        before_cl_df = pd.concat(frames)
    df = clean_data(curr_file, col_types)

    if __debug__:
        frames = [df, after_cl_df]
        after_cl_df = pd.concat(frames)

    print curr_file + " has been cleaned! \n"
    p_id = df[policy_ID]
    df = drop_columns(df, policy_ID)
    df = scaling(df)
    print "---------------------------->\n"
    print df.shape
    print len(p_id)
    #df = pd.concat([p_id, df], axis=1)
    save_data_frame(df, outfile + ntpath.basename(curr_file))
    print curr_file + " has been saved! \n"
print '\nDONE!\n'
            #if __debug__:
            #    print col_dict

print "---------------------------->\n"
print before_cl_df.shape
print "---------------------------->\n"
print df.shape
print "---------------------------->\n"
print set(before_cl_df.columns.values) - set(df.columns.values)



exit()
for col  in after_cl_df:
    print col
    if __debug__:
        if(df[col].dtype != 'object'):
            i+=1
            print 'Before Coding:'
            pd_before = pd.value_counts(before_cl_df[col])
            print pd_before
            print 'After Coding:'
            print pd.value_counts(after_cl_df[col])
