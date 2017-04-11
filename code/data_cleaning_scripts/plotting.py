import csv
from math import log
import numpy as np
from array import array
import pandas as pd
import math
import matplotlib.pyplot as plt


# ### scatter_plot function takes dataframe 'data' and x, y axis attribute names and plots data[y] on data[x]
def scatter_plot(data, x, y):
    f = plt.figure()
    ax = f.add_subplot(1, 1, 1)
    ax.scatter(data[x], data[y])
    plt.title(x + ' and ' + y + ' distribution')
    plt.xlabel(x)
    plt.ylabel(y)
    #plt.show()
    return f
#%matplotlib inline


# ### Usage example

# In[6]:

#fig = scatter_plot(sales, x = "Age", y = "Loss_Amount") 
#fig.show()


# ### box_whisher plot (/*this is again a good way to understand the data distribution, if you want to use*/)

# In[7]:

def boxWhisker_plot(data, x, y):
    ax = data.boxplot(y, x)
    plt.title(x + ' and ' + y + ' distribution')
    plt.xlabel(x)
    plt.ylabel(y)
    #plt.show()
    return plt


# In[1]:

#fig = boxWhisker_plot(sales, x ="Age", y = "Loss_Amount")



