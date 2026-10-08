import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s"
)

logger = logging.getLogger(__name__)


# More loops + functions

def get_positive_number():
    number = input("Enter a positive number: ")

    while not number.isdigit() or int(number) <= 0:
        logger.warning("Invalid input received")
        number = input("Please enter a valid positive number: ")

    logger.info(f"Valid number entered: {number}")
    return int(number)


def display_square(number):
    logger.info(f"Square: {number ** 2}")


user_number = get_positive_number()
display_square(user_number)