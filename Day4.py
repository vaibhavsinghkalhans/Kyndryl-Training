def display_inventory_items(items):
    for item in items:
        print(item)


def display_item_details(details_dict):
    for item, details in details_dict.items():
        print(f"{item} - Price: ₹{details['price']}, Stock: {details['stock']}")


def display_codes(codes):
    for code in codes:
        print(code)


def display_categories(category_set):
    for category in category_set:
        print(category)


inventory_items = ["Laptop", "Mouse", "Keyboard"]

item_codes = ("LP101", "MS102", "KB103")

item_details = {
    "Laptop": {"price": 50000, "stock": 10},
    "Mouse": {"price": 500, "stock": 50},
    "Keyboard": {"price": 1500, "stock": 20}
}

categories = {"Electronics", "Accessories"}

print("Inventory Items:")
display_inventory_items(inventory_items)

print("\nItem Details:")
display_item_details(item_details)

print("\nItem Codes:")
display_codes(item_codes)

print("\nCategories:")
display_categories(categories)