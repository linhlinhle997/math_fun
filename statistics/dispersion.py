from typing import List
import numpy as np
import math
from utils import sum_of_squares, de_mean

class Dispersion:
    Vector = List[float]

    def __init__(self, data: List[float]):
        self.data = data
    
    def data_range(self):
        """the data range is  the difference between the maximum and minimum values in the dataset"""
        # return np.ptp(data)
        result = max(self.data) - min(self.data)
        print("Data range: ", result)
        return 
    
    def sample_variance(self) -> float:
        """Sample variance quantifies the variability or dispersion of data points in a sample around the sample mean"""
        # return np.var(data, ddof=1)
        if len(self.data ) <= 2:
            raise "Variance requires at least two elements"
        n = len(self.data)
        deviations = de_mean(self.data)
        result = sum_of_squares(deviations) / (n - 1)
        print("Sample Variance: ", result)
        return result
    
    def standard_deviation(self):
        """Standard deviation is the square root of the variance, making it more interpretable"""
        # return np.std(self.data, ddof=1)
        result = math.sqrt(self.sample_variance())
        print("Standard deviation: ", result)
        return

        

    
    
        