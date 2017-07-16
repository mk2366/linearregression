import numpy as np


class LinearRegression():
   def train(self, X, T):
       """X is a matrix of samples - each row representing
       one measurement; T is a vector of measured results;
       both have to be a numpy array X of rank 2 and T of Rank 1"""
       n,m = X.shape
       _X = np.ones((n,m+1))
       _X[:,1:] = X
       self.w = np.linalg.solve(_X.T.dot(_X),_X.T.dot(T))
   def predict(self,x):
       """x is a list representing the data x1 ... xn"""
       _x = [1.00]
       _x.extend(x)
       _x = np.array(_x)
       return _x.dot(self.w)
