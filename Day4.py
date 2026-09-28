inventory = ["Laptop", "Mouse", "Keyboard"]

item_codes = ("LP101", "MS102", "KB103")

item_details = {
    "Laptop": {"price": 50000, "stock": 10},
    "Mouse": {"price": 500, "stock": 50},
    "Keyboard": {"price": 1500, "stock": 20}
}

categories = {"Electronics", "Accessories"}

for item in inventory:
    print(item)

for item, details in item_details.items():
    print(f"{item} - Price: ₹{details['price']}, Stock: {details['stock']}")

for code in item_codes:
    print(code)

for category in categories:
    print(category)