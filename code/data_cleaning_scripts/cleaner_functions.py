import csv
import ast
import sys
from math import log
import numpy as np
from array import array
import pandas as pd
import math
import matplotlib.pyplot as plt

def scaling(df): #df is dataframe, this method applies both scale in range and robust_scale methods
    from sklearn import preprocessing
    scaler = preprocessing.MinMaxScaler()
    df_scaled = preprocessing.robust_scale(df)

    df_scaled = pd.DataFrame(df_scaled, columns=df.columns.values)
    df_scaled = pd.DataFrame(scaler.fit_transform(df_scaled), columns=df.columns.values)
    return df_scaled

def drop_columns(df, cols):
    for col in df:
        if df[col].dtype == 'object':
            print "~~~~~~~~~~~~~~~~\n"
            print col
            print "~~~~~~~~~~~~~~~~\n"
            df = df.drop(col, 1)
    df = df.drop(cols, 1)
    return df

def coding(col, codeDict):
    colCoded = pd.Series(col, copy=True)
    for key, value in codeDict.items():
        colCoded.replace(key, value, inplace=True)
    return colCoded

def make_EEA_Prior_Bodily_Injury_Limit_numeric(el):
    if (el == '100-200'):
        el = 1
    elif (el == '100-400'):
        el = 2
    elif (el == '200-400'):
        el = 3
    elif (el == '20-50'):
        el = 4
    elif (el == '40-100 '):
        el = 5
    elif (el == '300-300'):
        el = 6
    elif (el == '750-750'):
        el = 7
    elif (el == '75-300'):
        el = 8
    else:
        el = 0 
    return el
def make_Policy_Zip_Code_Garaging_Location_numeric(el):
    if(el == 'Unknown'):
        el = 0
    else:
        el = int(el)/(100)
    return el

def make_Vehicle_New_Cost_Amount_numeric(el):
    if(el == -1):
        el = 0
    elif (el < 100):
        el = el*int(el)
    else:
        el = int(el)
    return el

def make_Vehicle_Make_Year_numeric(el):
    if(el == 'Unknown'):
        el = -1
    else:
        el = (2007-int(el))/10
    return el

def make_Vehicle_Symbol_numeric(el):
    if(el == -1):
        el = 0
    else:
        el = int(el)
    return el

#FIXME: 99 to 0??? isn't it mistke?
def make_Vehicle_Number_Of_Drivers_Assigned_numeric(el):
    if(el == 99):
        el = 0
    else:
        el = int(el)
    return el

#FIXME: ?? why 11?
def make_Vehicle_Miles_To_Work_numeric(el):
    if(el == -1):
       el = 11
    else:
       el = int(el)
    return el

def make_Vehicle_Days_Per_Week_Driven_numeric(el):
    if(el == -1):
        el = 0
    elif (el == 8) or (el == 8):
        el = 7
    else:
        el = int(el )
    return el

def make_Vehicle_Annual_Miles_numeric(el):
    if(el == 'Unknown'):
        el = 29555
    else:
        el = int(el)
    return el

def make_Vehicle_Med_Pay_Limit_numeric(el):
    if(el == -1):
        el = 0
    else:
        el = int(el)
    return el

def make_Vehicle_Bodily_Injury_Limit_numeric(el):
    if (el == '25-50  '):
        el = 1
    elif (el == '50-100 '):
        el = 2
    elif (el == '100-300'):
        el = 3
    elif (el == '100-500'):
        el = 4
    elif (el == '250-500'):
        el = 5
    elif (el == '300-500'):
        el = 6
    elif (el == '500-500'):
        el = 7
    elif (el == '1M-1M'):
        el = 8
    else:
        el = 0 
    return el

def make_Vehicle_Physical_Damage_Limit_numeric(el):
    if(el == -1):
        el = 0
    else:
        el = el 
    return el

def make_Vehicle_Comprehensive_Coverage_Limit_numeric(el):
    if(el == -1):
        el = 0
    else:
        el = el 
    return el

def make_Vehicle_Collision_Coverage_Deductible_numeric(el):
    if(el == -1):
        el = 0
    else:
        el = el 
    return el

def make_EEA_Policy_Zip_Code_3_numeric(el):
    if(el == 'Unknown'):
        el = 0
    else:
        el = int(el)/(100)
    return el

def make_EEA_Policy_Tenure_numeric(el):
    if(el == -1):
        el = 0
    elif (el > 0):
        el = int(el)/(10)+1
    else:
        el = el
    return el

#####################################################
#   \var path is the data file path
#   \vat col_types it is information about the type of the column
#   \ret returns the cleaned dataframe
#####################################################
def clean_data(path, col_types):
    #####################################################
    #  0.1 reading data into dataframe and names of the coulmns
    ####################################################
    df = pd.read_csv(path) # reading complete data
    cols = list(df.columns.values)
    ####################################################
    #
    #   1. DATA CLEANING PORTION
    #   1.0. Removing the dublicates
    #
    ####################################################
    policy_ID = 'PolicyNo' # name of the first column for identifying the policies
    cols.remove(policy_ID)
    df=df.drop_duplicates(cols)
    if __debug__:
        print len(df)
        print len(df)

    #------------------------------------------------------#
    #   -- debug the frequencies and the possible values-- #
    #------------------------------------------------------#
    __1debug__=False
    if __1debug__:
        for col_name in cols:
            if (col_name == policy_ID):
                continue
            frq = df.groupby(col_name)
            ## uncomment following codes to redirect frequncy information from std.out into the file
            pd.set_option('display.max_rows', len(frq.size())) ## this forces panda to print series fully
            sys.stdout = open(col_name + "__frequency.txt", 'w') # this redirect stdout to the file
            print frq.size()
            print "--------------------------------------------------------------"

    attr_name = 'Attribute Name'
    attr_type = 'Type'
    attr_dict = 'code_dictionary'
    if __debug__:
        i = 0
    for row in col_types.iterrows():
        if(row[1][attr_type] == 'toBinary' or row[1][attr_type] == 'toNumerical'):
            col_name = row[1][attr_name]
            col_dict = ast.literal_eval(row[1][attr_dict])

            #if __debug__:
            #    print col_dict
            #    pd_before = pd.value_counts(df[col_name])

            df[col_name] = coding(df[col_name], col_dict)

            #if __debug__:
            #    if(df[col_name].dtype == 'object'):
            #        i+=1
            #        print 'Before Coding:'
            #        print pd_before
            #        print 'After Coding:'
            #        print pd.value_counts(df[col_name])
            #    print row
    if __debug__:
        print i
    for col in df:
        if (col == 'Policy_Zip_Code_Garaging_Location'):
            df[col] = df[col].apply(make_Policy_Zip_Code_Garaging_Location_numeric)
        if (col== 'Vehicle_Make_Year'):
            df[col] = df[col].apply(make_Vehicle_Make_Year_numeric)
        if (col== 'Vehicle_New_Cost_Amount'):
            df[col] = df[col].apply(make_Vehicle_New_Cost_Amount_numeric)
        if (col== 'Vehicle_Symbol'):
            df[col] = df[col].apply(make_Vehicle_Symbol_numeric)
        if (col== 'Vehicle_Number_Of_Drivers_Assigned'):
            df[col] = df[col].apply(make_Vehicle_Number_Of_Drivers_Assigned_numeric)
        if (col== 'Vehicle_Miles_To_Work'):
            df[col] = df[col].apply(make_Vehicle_Miles_To_Work_numeric)
        if (col== 'Vehicle_Days_Per_Week_Driven'):
            df[col] = df[col].apply(make_Vehicle_Days_Per_Week_Driven_numeric)
        if (col== 'Vehicle_Annual_Miles'):
            df[col] = df[col].apply(make_Vehicle_Annual_Miles_numeric)
        if (col== 'Vehicle_Med_Pay_Limit'):
            df[col] = df[col].apply(make_Vehicle_Med_Pay_Limit_numeric)
        if (col== 'Vehicle_Bodily_Injury_Limit'):
            df[col] = df[col].apply(make_Vehicle_Bodily_Injury_Limit_numeric)
        if (col== 'Vehicle_Physical_Damage_Limit'):
            df[col] = df[col].apply(make_Vehicle_Physical_Damage_Limit_numeric)
        if (col== 'Vehicle_Comprehensive_Coverage_Limit'):
            df[col] = df[col].apply(make_Vehicle_Comprehensive_Coverage_Limit_numeric)
        if (col== 'Vehicle_Collision_Coverage_Deductible'):
            df[col] = df[col].apply(make_Vehicle_Collision_Coverage_Deductible_numeric)
        if (col== 'EEA_Policy_Zip_Code_3'):
            df[col] = df[col].apply(make_EEA_Policy_Zip_Code_3_numeric)
        if (col== 'EEA_Policy_Tenure'):
            df[col] = df[col].apply(make_EEA_Policy_Tenure_numeric)
        if (col== 'EEA_Prior_Bodily_Injury_Limit'):
            df[col] = df[col].apply(make_EEA_Prior_Bodily_Injury_Limit_numeric)

    print "dhshdjshfjksgdfksfksgdfgsdf\n"
    print df.shape
    return df

def save_data_frame(df, outfile):
    df.to_csv(outfile, index=False)
    if __debug__:
        print df.shape
