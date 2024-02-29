from typing import List
import numpy as np

Vector = List[float]


def dot(v: Vector, w: Vector) -> float:
    """Compute v_1*w_1 + ... + v_n*w*n"""
    if len(v) != len(w):
        raise ValueError("Vectors must be the same length")
    return sum(v_i*w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    """Return v_1*w_1 + ... + v_n*w_n"""
    return dot(v, v)


def de_mean(data: List[float]) -> List[float]:
    """Translate data by subtracting its mean (so the result has mean 0)"""
    data_bar = np.mean(data)
    return [x - data_bar for x in data]


def standard_deviation(data: List[float]):
    """Standard deviation is the square root of the variance, making it more interpretable"""
    return np.std(data, ddof=1) # Set ddof=1 for sample standard deviation