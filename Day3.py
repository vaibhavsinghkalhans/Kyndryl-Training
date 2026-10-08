import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(message)s"
)

def calculate_results(first_number, second_number):
    total = first_number + second_number
    product = first_number * second_number
    logging.info("Calculation completed successfully.")
    return total, product

try:
    user_name = input("Enter your name: ")
    logging.info(f"User entered name: {user_name}")

    first_number = float(input("Enter first number: "))
    logging.info(f"First number entered: {first_number}")

    second_number = float(input("Enter second number: "))
    logging.info(f"Second number entered: {second_number}")

    sum_result, product_result = calculate_results(first_number, second_number)

    print("\n--- Results ---")
    print(f"Hello, {user_name}!")
    print(f"First Number : {first_number}")
    print(f"Second Number: {second_number}")
    print(f"Sum          : {sum_result}")
    print(f"Product      : {product_result}")

except ValueError:
    logging.error("Invalid input! Please enter numeric values for the numbers.")