
from typing import List
from utils import dot, de_mean, standard_deviation
import matplotlib.pyplot as plt

class Correlation:
    def __init__(self, data: List[float], data1: List[float]):
        self.data = data
        self.data1 = data1
    
    def covariance(self) -> float:
        """
        Covariance, the paired analogue of variance. Whereas variance measures how a single variable deviates from its mean, 
        covariance measures how two variables vary in tandem from their means
        """
        if len(self.data) != len(self.data1):
            return ValueError("data and data1 must have same number of elements")
        result = dot(de_mean(self.data), de_mean(self.data1)) / (len(self.data) - 1)
        print("Covariance: ", result)
        return result

    def correlation(self):
        """Correlation measures the strength and direction of the linear relationship between two variables"""
        stdev_data = standard_deviation(self.data)
        stdev_data1 = standard_deviation(self.data1)
        if stdev_data > 0 and stdev_data1 > 0:
            result = self.covariance() / stdev_data / stdev_data1
            print("Correlation: ", result)
        else:
            print("Correlation: 0") # if no variation, correlation is zero
        
        # Create a scatter plot
        self._plot()
            
    def _plot(self):
        plt.scatter(self.data, self.data1)
        plt.xlabel("# of data")
        plt.ylabel("# of data1")
        plt.title("Scatter plot with outlier and correlation")
        plt.show()
        