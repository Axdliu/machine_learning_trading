# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:57:38 2017
tutorial of sklearn
http://scikit-learn.org/stable/tutorial/basic/tutorial.html#machine-learning-the-problem-setting
@author: arnoleu
"""

# loading dataset

from sklearn import datasets

iris = datasets.load_iris()
digits = datasets.load_digits()

'''
in the case of the digits dataset, 
digits.data gives access to the features that can be used to classify the digits samples
'''

print digits.data
print digits.target

# learning and predict

from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
clf.predict(digits.data[-1:])

# model persistence

from sklearn import svm
from sklearn import datasets

clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)  

import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(X[0:1])
print y[0]

from sklearn.externals import joblib
joblib.dump(clf, 'filename.pkl')

# Conventions

import numpy as np
from sklearn import random_projection

rng = np.random.RandomState(0)
X = rng.rand(10, 2000)
X = np.array(X, dtype='float32')

