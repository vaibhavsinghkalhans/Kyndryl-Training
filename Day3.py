def calculate_results(first_number, second_number):
    total = first_number + second_number
    product = first_number * second_number
    return total, product


user_name = input("Enter your name: ")

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

sum_result, product_result = calculate_results(first_number, second_number)

print("\n--- Results ---")
print(f"Hello, {user_name}!")
print(f"First Number : {first_number}")
print(f"Second Number: {second_number}")
print(f"Sum          : {sum_result}")
print(f"Product      : {product_result}")