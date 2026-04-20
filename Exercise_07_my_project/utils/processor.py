from utils.data_handler import save_data
import os

DATA_DIR = "data"
MAX_PRODUCTS = 50
MY_PROJECT_FILE = os.path.join(DATA_DIR, "my_project.json")


def add_product(
    products_list, product_name, current_price, target_price, currency, tags=None
):
    # add a new product to the products list
    if len(products_list) >= MAX_PRODUCTS:
        print(f"Too many products added. Maximum allowed products is {MAX_PRODUCTS}")
        return

    new_product = {
        "ProductName": product_name,
        "CurrentPrice": current_price,
        "TargetPrice": target_price,
        "Currency": currency,
        "tags": tags if tags else [],
    }

    products_list.append(new_product)
    print(f"[ADDED] {product_name} is added to Price Tracking list")
    save_data(products_list, MY_PROJECT_FILE)


def list_all_products(products_list):
    """Print all products sorted alphabetically by Product Name."""

    if not products_list:
        print("[EMPTY] No products added yet.")
        return
    sorted_products = sorted(products_list, key=lambda r: r["ProductName"])
    print(f"\n=== All Records ({len(sorted_products)}) ===")
    for product in sorted_products:
        print(f" {product['ProductName']}")
        for key, value in product.items():
            if key != "ProductName":
                print(f" {key}: {value}")


# Use .get() for every field — safe access even if a field is missing


def search_products(products_list, search_term):
    """returns a list whose title contains the search term"""
    results = [
        product
        for product in products_list
        if search_term.lower() in product["ProductName"].lower()
    ]
    return results


def display_tags(products_list):
    """Returns a set of unique tags used across all the products"""
    all_tags = set()
    for product in products_list:
        for tag in product.get("tags", []):
            all_tags.add(tag)
    return all_tags
