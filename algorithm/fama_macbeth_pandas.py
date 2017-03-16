# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 23:33:59 2017
a test of fama_macbeth model in pandas

@author: User
"""

import pandas as pd
import numpy as np


y = [0.1, 0.3, 0.4, 0.0, 0.2, 0.4, 0.2, 0.1, 0.4, 0.6, 0.7, 0.4]
x = [0.4, 0.6, 0.2, 1.2, 0.7, 0.5, 0.1, 0.0, 0.8, 0.1, 0.6, -0.1]

id_u = ['1','2','3','4']
date_u = ['2012-01-01', '2012-02-01', '2012-03-01']
id_f = id_u*3
date_f = sorted(date_u*4)
arrays = np.array([date_f,id_f])
index = pd.MultiIndex.from_arrays(arrays, names=['date', 'id'])
data = np.array([x,y]).T
df = pd.DataFrame(data, index=index, columns = ['x', 'y'])

# The fama_macbeth function expects the y-var and x-vars to have a multi-index 
# with date as the first variable and the stock/firm/entity 
# id as the second variable in the index:
fm  = pd.fama_macbeth(y=df['y'],x=df[['x']])