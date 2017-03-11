# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 20:40:05 2017
a sample of Genetic Algorithm
http://iamtrask.github.io/2015/07/12/basic-python-network/

@author: User
"""
import numpy as np

    
# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

# input dataset
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])

# output dataset           
y = np.array([[0,0,1,1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
# "syn0" to imply "synapse zero". 
# Since we only have 2 layers (input and output), 
# we only need one matrix of weights to connect them.
syn0 = 2*np.random.random((3,1)) - 1

for iter in xrange(10000):
    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    # how much did we miss?
    l1_error = y - l1
    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    # reducing the error of high confidence predictions
    l1_delta = l1_error * nonlin(l1,True)

    # update weights
    syn0 += np.dot(l0.T,l1_delta)

print "Output After Training:"
print l1