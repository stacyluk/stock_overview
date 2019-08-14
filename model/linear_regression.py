import numpy as np
from numpy.linalg import inv


class CommonLinearRegressor:
    def __init__(self, C=1):
        self.coef = None
        self.C = C

    def fit(self, X, y):
        n_objects = X.shape[0]
        n_features = X.shape[1]
        
        eye = np.ones((n_objects, 1))
        X_ = np.concatenate((eye, X), axis=1)
        self.coef = inv(X_.T @ X_ + self.C * np.eye(n_features + 1)) @ X_.T @ y.T

    def predict(self, X):
        eye = np.ones((X.shape[0], 1))
        X_ = np.concatenate((eye, X), axis=1)
        return (X_ @ self.coef)

    def __setstate__(self, d):
        self.C = d['C']
        self.coef = np.array(d['coef'])

    def __getstate__(self):
        return {'C': self.C, 'coef': list(self.coef)}

