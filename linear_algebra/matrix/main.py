import argparse
import ast
from typing import List
from matrix import Matrix, CreateMatrix

def check_args(parser: argparse.ArgumentParser, args: argparse.Namespace):
    """Check if --i is provided when --op and 'get_row' and 'get_column'."""
    if args.op in ["get_row", "get_column"]:
        if not args.i:
            parser.error("--i is required when --op is 'get_row' or 'get_column")

    if args.op == "r_c_matrix":
        if not args.r or not args.c:
            parser.error("--r or --c is required when --op is 'r_c_matrix")

def parse_generic_matrix(s: str, element_type=None) -> List[List[float]]:
    try:
        parsed_value = ast.literal_eval(s)
        if not isinstance(parsed_value, list):
            raise ValueError("Invalid matrix format")
        if not all(isinstance(row, list) for row in parsed_value):
            raise ValueError("Invalid matrix format: rows must be lists")

        if element_type is not None:
            for row in parsed_value:
                if not all(isinstance(elem, element_type) for elem in row):
                    raise ValueError(f"All elements in the matrix must be of type {element_type}")

        return parsed_value

    except (ValueError, SyntaxError):
        raise argparse.ArgumentTypeError(f"Invalid matrix literal: {s}")


def perform_vector_operation(args: argparse.Namespace) -> List:
    matrix = Matrix(args.m)
    matrix_with_index = Matrix(args.m, args.i)
    create_matrix = CreateMatrix(args.n, args.r, args.c)

    operations = {
        "shape": matrix.shape,
        "get_row": matrix_with_index.get_row,
        "get_column": matrix_with_index.get_column,
        "r_c_matrix": create_matrix.r_c_matrix,
        "identity_matrix": create_matrix.identity_matrix
    }

    if args.op not in operations:
        raise ValueError("Invalid operation")

    return operations[args.op]()


def main() -> None:
    parser = argparse.ArgumentParser(description="Perform vector operations.")
    parser.add_argument("--m", type=parse_generic_matrix, help="Matrix")
    parser.add_argument("--i", type=int, help="Index")
    parser.add_argument("--r", type=int, help="Number of rows of matrix")
    parser.add_argument("--c", type=int, help="Number of columns of matrix")
    parser.add_argument("--n", type=int, help="Create n x n identity matrix")
    parser.add_argument("--op", choices=["shape", "get_row", "get_column", "identity_matrix", "r_c_matrix"], 
                        required=True, help="Operation to perform")
    args = parser.parse_args()

    check_args(parser, args)

    try:
        perform_vector_operation(args)
    except argparse.ArgumentError as e:
        parser.error(str(e))
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()