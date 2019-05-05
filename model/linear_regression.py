import numpy as np
from numpy.linalg import inv



class NaiveLinearRegressor:
    def __init__(self):
        self.coef = np.zeros(2)

    def fit(self, X, y):
        A = np.array([[(X**2).sum(), X.sum()],
                      [ X.sum(), X.shape[0] ]])
        
        B = np.array([(X * y).sum(),
                       y.sum()])
        self.coef = B.T @ inv(A)

    def predict(self, X):
        a, b = self.coef
        return (a * X + b)


class CommonLinearRegressor:
    def __init__(self):
        self.coef = None

    def fit(self, X, y):
        n_objects = X.shape[0]
        
        eye = np.ones((n_objects, 1))
        X_ = np.concatenate((eye, X), axis=1)
        self.coef = inv(X_.T @ X_) @ X_.T @ y.T

    def predict(self, X):
        eye = np.ones((X.shape[0], 1))
        X_ = np.concatenate((eye, X), axis=1)
        return (X_ @ self.coef)


