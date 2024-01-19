from typing import List
from vectors import Vectors


class ListVectors:
    Vector = List[float]

    def __init__(self, vectors: List[Vector]):
        self.vectors = vectors

    def vector_sum(self) -> Vector:
        """Add corresponding elements"""
        self._check_vector_lenghts
        return [sum(v_i) for v_i in zip(*self.vectors)]

    def vector_subtract(self) -> Vector:
        """Subtract corresponding elements"""
        self._check_vector_lenghts
        return [v_i[0] - sum(v_i[1:]) for v_i in zip(*self.vectors)]

    def vector_mean(self) -> Vector:
        """Compute the elements-wise average"""
        n = len(self.vectors)
        return self._scalar_multiply(1/n)

    def _scalar_multiply(self, c: float) -> Vector:
        """Multiplies every elements by c"""
        return [c*v_i for v_i in self.vector_sum()]

    def _check_vector_lenghts(self):
        """Check that vectors have the same length"""
        num_elements = len(vectors[0])
        assert all(len(v) == num_elements for v in vectors), "Vectors must be the same lenght"
