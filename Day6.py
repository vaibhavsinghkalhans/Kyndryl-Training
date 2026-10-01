# More loops + functions

def get_positive_number():
    number = input("Enter a positive number: ")

    while not number.isdigit() or int(number) <= 0:
        number = input("Please enter a valid positive number: ")

    return int(number)


def display_square(number):
    print(f"Square: {number ** 2}")


user_number = get_positive_number()
display_square(user_number)