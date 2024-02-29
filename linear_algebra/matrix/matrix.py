from typing import Tuple, List, Callable

class Matrix:
    Matrix = List[List[float]]
    Vector = List[float]
    
    def __init__(self, A: Matrix, index: int = None):
        self.A = A
        self.index = index
    
    def shape(self) -> Tuple[int, int]:
        """Return (# of rows of A, # of columns of A)"""
        num_rows = len(self.A)
        num_cols = len(self.A[0] if self.A else 0)
        print(f"{num_rows} rows, {num_cols} columns")
        return num_rows, num_cols
    
    def get_row(self) -> Vector:
        """Returns i-th row of A (as a Vector)"""
        row_at_i = self.A[self.index]
        print(f"Row at index {self.index} is {row_at_i}")
        return row_at_i
    
    def get_column(self) -> Vector:
        """Return the i-th column of A (as a Vector)"""
        col_at_i = [A_i[self.index] for A_i in self.A]
        print(f"Column at index {self.index} is {col_at_i}")
        return col_at_i
    

class CreateMatrix:
    Matrix = List[List[float]]
    
    def __init__(self, num: int = None, num_rows: int = None, num_cols: int = None):
        self.num = num
        self.num_rows = num_rows
        self.num_cols = num_cols
        
    def r_c_matrix(self) -> Matrix:
        """Returns the r x c matrix"""
        matrix = self._make_matrix(self.num_rows, self.num_cols, lambda i, j: i + j)
        print(matrix)
        return matrix
        
    def identity_matrix(self) -> Matrix:
        """Returns the n x n identity matrix"""
        matrix = self._make_matrix(self.num, self.num, lambda i, j: 1 if i == j else 0)
        print(matrix)
        return matrix
    
    @staticmethod
    def _make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Matrix:
        """
        Return a num_rows x num_cols matrix
        whose (i, j)-th entry is entry_fn(i, j)
        """
        return [[entry_fn(i, j)              # given i, create a list
                for j in range(num_cols)]   # [entry_fn(i, 0), ...]
                for i in range(num_rows)]   # create one list for each i