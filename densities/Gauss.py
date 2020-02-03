import numpy as np
from scipy.stats import norm

class Gauss:
    def __init__(self, mean=[0], cov=[[1]]):
        self.mean = np.asarray(mean)
        self.cov  = np.asarray(cov)
        self.dim  = len(self.mean)

    def evaluate(self, point):
        return norm.pdf(point)