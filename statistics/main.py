import argparse
from typing import List
from central_tendencies import CentralTendency
from dispersion import Dispersion
from correlation import Correlation

def check_args(parser: argparse.ArgumentParser, args: argparse.Namespace):
    """Check if --f1 is provided when --op is 'covariance'."""
    if args.op == "covariance":
        if not args.f1:
            parser.error("--f1 is required when --op is 'covariance")


def read_data_from_file(file_path: str) -> List[float]:
    """Read data from file and return as a list of floats."""
    try: 
        with open(file_path, 'r') as f:
            data = f.read()
            data_list = [float(x) for x in data.split(',') if x.strip()]
            return data_list
    except FileNotFoundError:
        print("File Not Found")
        return []
    except Exception as e:
        print("An error occurred: ", e)
        return []
    
    
def perform_vector_operation(data: List[float], operation: str, data1: List[float] = None):
    """Perform vector operations based on the provided arguments."""
    central_tendency = CentralTendency(data)
    dispersion = Dispersion(data)
    correlation = Correlation(data, data1)

    operations = {
        "describe": central_tendency.describe,
        "data_range": dispersion.data_range, 
        "variance": dispersion.sample_variance,
        "standard_deviation": dispersion.standard_deviation,
        "covariance": correlation.covariance,
        "correlation": correlation.correlation,
    }

    if operation not in operations:
        raise ValueError("Invalid operation")

    return operations[operation]()


def main() -> None:
    parser = argparse.ArgumentParser(description="Perform vector operations.")
    parser.add_argument("--f", required=True, help="Path to the file containing data")
    parser.add_argument("--f1", help="Path to the file containing data")
    parser.add_argument("--op", choices=["describe", "data_range", "variance", "standard_deviation",
                                         "covariance", "correlation"], 
                        required=True, help="Operation to perform")
    args = parser.parse_args()
    
    check_args(parser, args)
    
    data = read_data_from_file(args.f)
    data1 = read_data_from_file(args.f1) if args.f1 else None

    try:    
        perform_vector_operation(data, args.op, data1)
    except argparse.ArgumentError as e:
        parser.error(str(e))
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()