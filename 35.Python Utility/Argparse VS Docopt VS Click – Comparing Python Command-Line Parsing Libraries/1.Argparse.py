# argparse_example.py

import argparse

if __name__ == '__main__':

    # Initialize
    parser = argparse.ArgumentParser(description="Simple calculator")

    # Adding optional parameters
    parser.add_argument('-n1',
                        '--num1',
                        help="Number 1",
                        type=float)

    parser.add_argument('-n2',
                        '--num2',
                        help="Number 2",
                        type=float)

    parser.add_argument('-op',
                        '--operation',
                        help="operator",
                        default="*")

    # Parsing the argument
    args = parser.parse_args()
    print(args)

    # Initialize result to None
    result = None

    # Simple calculator operations
    if args.operation == '+':
        result = args.num1 + args.num2

    if args.operation == '-':
        result = args.num1 - args.num2

    if args.operation == '/':
        result = args.num1 / args.num2

    if args.operation == '*':
        result = args.num1 * args.num2

    if args.operation == 'pow':
        result = pow(args.num1, args.num2)

    # Print the result
    print("Result = ", result)
