# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:25:40 2017
refitting and updating parameters

@author: arnoleu
"""

import numpy as np
from sklearn.svm import SVC

rng = np.random.RandomState(0)
X = rng.rand(100, 10)
y = rng.binomial(1, 0.5, 100)
X_test = rng.rand(5, 10)

clf = SVC()
clf.set_params(kernel='linear').fit(X, y)  
print clf.predict(X_test)
clf.set_params(kernel='rbf').fit(X, y)
print clf.predict(X_test)  
