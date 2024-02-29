from collections import Counter
from typing import List
import matplotlib.pyplot as plt
import numpy as np

class CentralTendency:
    def __init__(self, data: List[float]):
        self.data = data
    
    def describe(self):
        """Calculate basic statistics"""
        num_data = len(self.data)
        largest_value = max(self.data)
        smallest_value = min(self.data)
        
        print("Number of data points:", num_data)
        print("Largest value:", largest_value)
        print("Smallest value:", smallest_value)
        print("Mean value:", self._mean())
        print("Median value:", self._median())
        print("Mode value:", self._mode())
        print("First quartile (Q1): ", self._quantiles(0.25))
        print("Third quartile (Q3): ", self._quantiles(0.75))
        
        # Plot histogram and box plot with quantiles
        self._plot_and_quantiles()
        return
        
    def _plot_and_quantiles(self):
        """Plot histogram and box plot with quantiles"""
        # Create subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
        
        # PLot data histogram
        count_data = Counter(self.data)
        largest_value= int(max(self.data))
        xs = range(largest_value + 5)
        ys = [count_data[x] for x in xs]
        ax1.bar(xs, ys)
        ax1.axis([0, largest_value + 5, 0, max(ys) + 5])
        ax1.set_title("Histogram of data Counts")
        ax1.set_xlabel("Value")
        ax1.set_ylabel("Frequency")
        
        # Plot box plot with quantiles  
        quantiles = np.percentile(self.data, [25, 75]) 
        ax2.boxplot(self.data, vert=False)
        ax2.scatter(quantiles, [1, 1], color='red', marker='o', label="Quantiles")
        ax2.set_xlabel("Values")
        ax2.set_title("Box plot with Quantiles")
        ax2.legend()
        
        # Show the plot
        plt.show()
        return

    def _quantiles(self, p: float) -> float:
        """Quantiles are values that divide a dataset into equal-sized subsets"""
        # return np.quantile(self.data, p)
        p_index = int(p*len(self.data))
        result = sorted(self.data)[p_index]
        return result
    
    def _mean(self) -> float:
        """The mean is the average value of a dataset"""
        # return np.mean(self.data)
        return sum(self.data)/len(self.data)

    def _median(self) -> float:
        """The median is the middle value of a dataset when it is arranged in ascending order"""
        # return np.median(self.data)
        return self.__median_even() if len(self.data) % 2 == 0 else self.__median_odd()
    
    def _mode(self) -> List[float]:
        """The mode is the value that appears most frequently in a dataset"""
        # return np.mode(self.data)
        counts = Counter(self.data)
        max_count = max(counts.values())
        return [x_i
                for x_i, count in counts.items()
                if count == max_count]
        
    def __median_odd(self) -> float:
        """ If the dataset has an odd number of values, the median is the middle value"""
        return sorted(self.data)[len(self.data) // 2]
    
    def __median_even(self) -> float:
        """ If the dataset has an even number of values, the median is the average of the two middle values"""
        sorted_x = sorted(self.data)
        hi_midpoint = len(self.data) // 2  # e.g. Length 4 -> hi_midpoint 2
        return (sorted_x[hi_midpoint - 1] + sorted_x[hi_midpoint]) / 2
