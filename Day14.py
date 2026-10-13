import argparse

def add_numbers(a, b):
    return a + b

parser = argparse.ArgumentParser(description="Add two numbers")

parser.add_argument(
    "--num1",
    type=int,
    default=10,
    help="First number"
)

parser.add_argument(
    "--num2",
    type=int,
    default=20,
    help="Second number"
)

args = parser.parse_args()

result = add_numbers(args.num1, args.num2)

print("Result:", result)