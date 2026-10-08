import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(message)s"
)

def display_inventory_items(items):
    logging.info("Displaying inventory items")
    for item in items:
        print(item)

def display_item_details(details_dict):
    logging.info("Displaying item details")
    for item, details in details_dict.items():
        print(f"{item} - Price: ₹{details['price']}, Stock: {details['stock']}")

def display_codes(codes):
    logging.info("Displaying item codes")
    for code in codes:
        print(code)

def display_categories(category_set):
    logging.info("Displaying categories")
    for category in category_set:
        print(category)

try:
    inventory_items = ["Laptop", "Mouse", "Keyboard"]

    item_codes = ("LP101", "MS102", "KB103")

    item_details = {
        "Laptop": {"price": 50000, "stock": 10},
        "Mouse": {"price": 500, "stock": 50},
        "Keyboard": {"price": 1500, "stock": 20}
    }

    categories = {"Electronics", "Accessories"}

    logging.info("Inventory loaded successfully")

    print("Inventory Items:")
    display_inventory_items(inventory_items)

    print("\nItem Details:")
    display_item_details(item_details)

    print("\nItem Codes:")
    display_codes(item_codes)

    print("\nCategories:")
    display_categories(categories)

except Exception as e:
    logging.error(f"An error occurred: {e}")