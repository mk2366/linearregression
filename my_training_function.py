import numpy as np


class LinearRegression():
   def train(self, X, T):
      self.w = np.linalg.solve(X.T.dot(X),X.T.dot(T))
   def predict(self,X):
       return X.dot(self.w)
