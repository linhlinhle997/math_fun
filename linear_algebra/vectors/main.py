import argparse
import ast
from typing import List
from vectors import Vectors
from listvectors import ListVectors


def parse_generic_list(s: str, element_type=None) -> List:
    try:
        parsed_value = ast.literal_eval(s)
        if not isinstance(parsed_value, list):
            raise ValueError("Invalid list format")
        if element_type is not None and not all(isinstance(elem, element_type) for elem in parsed_value):
            raise ValueError(f"All elements in the list must be of type {element_type}")

        return parsed_value

    except (ValueError, SyntaxError):
        raise argparse.ArgumentTypeError(f"Invalid list literal: {s}")


def validate_vector_list(args: argparse.Namespace, operation: str) -> None:
    if operation in ["vector_sum", "vector_subtract", "vector_mean"]:
        if not all(isinstance(v, list) for v in args.v):
            raise argparse.ArgumentTypeError("--v must be a list of lists for the selected operation.")


def perform_vector_operation(args: argparse.Namespace) -> List:
    vectors_instance = Vectors(args.v, args.w)
    list_vectors_instance = ListVectors(args.v)

    operations = {
        "add": vectors_instance.add,
        "subtract": vectors_instance.subtract,
        "multi": vectors_instance.multi,
        "dot": vectors_instance.dot,
        "magnitude": vectors_instance.magnitude,
        "distance": vectors_instance.distance,
        "vector_sum": list_vectors_instance.vector_sum,
        "vector_subtract": list_vectors_instance.vector_subtract,
        "vector_mean": list_vectors_instance.vector_mean
    }

    if args.op not in operations:
        raise ValueError("Invalid operation")

    return operations[args.op]()


def main() -> None:
    parser = argparse.ArgumentParser(description="Perform vector operations.")
    parser.add_argument("--v", type=parse_generic_list, required=True, help="Elements of the first vector")
    parser.add_argument("--w", type=parse_generic_list, help="Elements of the second vector")
    parser.add_argument("--op", choices=["add", "subtract", "multi", "dot", "magnitude" , "distance",
                                         "vector_sum", "vector_subtract", "vector_mean"], 
                        required=True, help="Operation to perform")
    args = parser.parse_args()
    
    try:
        validate_vector_list(args, args.op)
        result = perform_vector_operation(args)
        print(result)
    except argparse.ArgumentError as e:
        parser.error(str(e))
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()