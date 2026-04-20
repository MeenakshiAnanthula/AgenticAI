import csv
import json


def create_csv(products_list, file_name):
    """export to a CSV file"""

    with open(file_name, "w", newline="", encoding="utf-8") as csv_file:
        # DictWriter uses column names — much safer than writing raw comma-separated values
        field_names = [
            "ProductName",
            "CurrentPrice",
            "TargetPrice",
            "Currency",
            "tags",
        ]
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()  # Write the column name row first
        writer.writerows(products_list)
    print(f"[Pipeline] Created: {file_name} with {len(products_list)} product records.")


def save_data(products, file_name):
    try:
        with open(file_name, "w", newline="", encoding="UTF-8") as json_file:
            json.dump(products, json_file, indent=2)
        print(f"[Pipeline] written {len(products)} products to {file_name}")
    except FileNotFoundError:
        print(f"[Pipeline] Error: {file_name} File not found")


def load_data(file_name):
    try:
        with open(file_name, "r", encoding="UTF-8") as json_file:
            products = json.load(json_file)
            # products = list(reader)
            print(f"[Pipeline] Read:{len(products)} products from {file_name}")
            # print(json.dumps(data, indent=2))
        return products
    except FileNotFoundError:
        print(f"[Pipeline] Error: {file_name} file not found")
        print("No existing data. Starting fresh.")
        products = []
        return products

    except json.JSONDecodeError:
        print(f"[Pipeline] Error: {file_name} failed to decode the json file")
