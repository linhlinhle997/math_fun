from typing import List
import math

class Vectors:
    Vector = List[float]

    def __init__(self, v: Vector, w: Vector):
        self.v = v
        self.w = w
    
    def add(self) -> Vector:
        """Add corresponding elements"""
        self._check_vector_length()
        return [v_i + w_i for v_i, w_i in zip(self.v, self.w)]

    def subtract(self) -> Vector:
        """Subtract corresponding elements"""
        self._check_vector_length()
        return [v_i - w_i for v_i, w_i in zip(self.v, self.w)]
    
    def multi(self) -> Vector:
        """Subtract corresponding elements"""
        self._check_vector_length()
        return [v_i * w_i for v_i, w_i in zip(self.v, self.w)]
    
    def dot(self, subtract: Vector = None) -> float:
        """Computes v_i*w_i + ... + v_n*w_n"""
        v = subtract if subtract is not None else self.v
        w = subtract if subtract is not None else self.w
        print(v, w)
        self._check_vector_length(v, w)
        return sum(v_i * w_i for v_i, w_i in zip(v, w))
    
    def magnitude(self) -> float:
        """
        Returns the magnitude (or length of v)
        sqrt(v[0]^2 + v[1]^2 + ... + w[n])^2)
        """
        return math.sqrt(self._sum_of_squares(self.v))

    def distance(self) -> float:
        """
        Computes the distance between v and w
        sqrt((v[0] - w[0])^2 + (v[1] - w[1])^2 + ... + (v[n-1] - w[n-1])^2)
        """
        squared_distance = self._sum_of_squares(self.subtract()) # (v_1-w_1)**(v_1-w_1) + ... + (v_n-w_n)**(v_n-w_n)
        return math.sqrt(squared_distance) 

    def _sum_of_squares(self, subtract: Vector = None) -> float:
        """Return the sum of squares of the vector elements"""
        v = subtract if subtract is not None else self.v
        return self.dot(v)

    def _check_vector_length(self, v=None, w=None):
        """Check that vectors have the same length"""
        v = v if v is not None else self.v
        w = w if w is not None else self.w
        assert len(v) == len(w), "Vectors must be the same length"
