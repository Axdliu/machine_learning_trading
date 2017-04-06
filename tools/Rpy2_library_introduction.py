# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 23:57:59 2017
using r from Python

@author: User
"""

import rpy2.robjects as robjects

pi = robjects.r['pi']
print pi