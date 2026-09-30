# More loops + functions

def get_number():
    num = input("Enter a positive number: ")
    while not num.isdigit() or int(num) <= 0:
        num = input("Enter a positive number: ")
    return int(num)

def display_square(n):
    print("Square:", n * n)

number = get_number()
display_square(number)