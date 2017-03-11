# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 15:22:32 2017
replicate neutral network from memory

@author: User
"""

import numpy as np

# input dataset
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])

# output dataset           
y = np.array([[0,0,1,1]]).T

#sigmoid function
def nonline(x, deriv=False):
    if deriv:
        return x*(1-x)
    return 1/(1+np.exp(-x))

syn0 = 2*np.random.random((3,1)) - 1   
    
for i in xrange(10000):
    l0 = X
    l1 = nonline(np.dot(l0, syn0))
    l1_error = l1 - y
    l1_delta = l1_error * nonline(l1, deriv=True)
    syn0 += np.dot(l0.T,l1_delta)
    
print l1