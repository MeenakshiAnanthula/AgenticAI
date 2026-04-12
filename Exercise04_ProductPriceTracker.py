"""Session 04 — Data Structures Deep Dive Agentic AI Builders Fellowship ·
Phase 1: Python for AI
My domain: [Product Price Tracker]"""

# setting named constant
MAX_PRODUCTS = 50

products = [
    {
        "ProductName": "IPhone",
        "CurrentPrice": "36000",
        "TargetPrice": "25000",
        "Currency": "NTD",
        "tags": ["electronics", "smartphone", "iphone"],
    },
    {
        "ProductName": "Samsung S26",
        "CurrentPrice": "39000",
        "TargetPrice": "32000",
        "Currency": "NTD",
        "tags": ["electronics", "smartphone", "samsung"],
    },
    {
        "ProductName": "Prada Handbag",
        "CurrentPrice": "500",
        "TargetPrice": "300",
        "Currency": "USD",
        "tags": ["accessories", "women", "handbags"],
    },
    {
        "ProductName": "Coach Wristwatch",
        "CurrentPrice": "1000",
        "TargetPrice": "800",
        "Currency": "USD",
        "tags": ["accessories", "women", "watches"],
    },
    {
        "ProductName": "Chicco Stroller",
        "CurrentPrice": "15000",
        "TargetPrice": "10000",
        "Currency": "NTD",
        "tags": ["baby", "stroller", "chicco"],
    },
    {
        "ProductName": "Globber trike",
        "CurrentPrice": "15000",
        "TargetPrice": "10000",
        "Currency": "INR",
        "tags": ["baby", "cycle", "trike", "Globber"],
    },
    {
        "ProductName": "LG Wash Tower",
        "CurrentPrice": "3000",
        "TargetPrice": "2000",
        "Currency": "EUR",
        "tags": ["home", "appliances", "clothes"],
    },
]


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


def main():
    """Run a demo of the full data model"""
    print(f"=== {__file__} — Session 04 Demo ===\n")

    # show starting data
    list_all_products(products)

    # Add a new product
    print("\n========== Adding a new Product ==========")
    add_product(
        products,
        "LG Refrigerator",
        "50000",
        "43000",
        "INR",
        tags=["home", "appliances", "food"],
    )

    # Search for a product
    print("\n========== Searching for LG=============")
    results = search_products(products, "LG")
    for r in results:
        print(f"Found: {r['ProductName']}")

    # Show unique tags set
    print("\n========== All unique tags============")
    unique_tags = display_tags(products)
    print(f"Tags: {sorted(unique_tags)}")


if __name__ == "__main__":
    main()
