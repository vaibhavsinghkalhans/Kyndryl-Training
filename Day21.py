import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def validate_age(age):
    return age.isdigit() and int(age) > 0

def mock_api(name, age):
    return {
        "status": "success",
        "message": f"Student {name} ({age} years old) registered successfully"
    }

# Input
name = input("Enter student name: ")
age = input("Enter age: ")

# Validation
if not validate_age(age):
    print("Invalid age entered!")
    logging.error("Invalid age entered")
else:
    # API Mock
    response = mock_api(name, age)

    # Logging
    logging.info(f"Student registered: {name}")

    # Output
    print("\nRegistration Result")
    print(response["message"])