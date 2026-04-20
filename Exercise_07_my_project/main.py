from utils.data_handler import create_csv, save_data, load_data
from utils.processor import (
    add_product,
    list_all_products,
    search_products,
    display_tags,
)
import os
from tabulate import tabulate

DATA_DIR = "data"
MY_PROJECT_FILE = os.path.join(DATA_DIR, "my_project.json")
OUTPUT_CSV_FILENAME = os.path.join(DATA_DIR, "products.csv")


def print_summary_table(processed_records):
    rows = [
        [
            r["ProductName"],
            r["CurrentPrice"],
            r["TargetPrice"],
            r["Currency"],
            r["tags"],
        ]
        for r in processed_records
    ]
    headers = ["Product Name", "Current Price", "Target Price", "Currency", "Tags"]
    print("\n" + tabulate(rows, headers=headers, tablefmt="grid"))


def run_pipeline():
    print("=" * 50)
    print("Product Price Tracking Pipeline")
    print("=" * 50)

    products = []

    # load data
    print("Loading data from json file")
    products = load_data(MY_PROJECT_FILE)
    list_all_products(products)

    # Add a new product
    """print("\n========== Adding a new Product ==========")
    add_product(
        products,
        "Sony Earbuds",
        "5000",
        "3000",
        "INR",
        tags=["electronics", "appliances", "earbuds"],
    )"""

    create_csv(products, OUTPUT_CSV_FILENAME)

    # Search for a product
    print("\n========== Searching for LG=============")
    results = search_products(products, "LG")
    for r in results:
        print(f"Found: {r['ProductName']}")

    # Show unique tags set
    print("\n========== All unique tags============")
    unique_tags = display_tags(products)
    print(f"Tags: {sorted(unique_tags)}")

    # save_data(products, MY_PROJECT_FILE)
    print_summary_table(products)


if __name__ == "__main__":
    run_pipeline()
