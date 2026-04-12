print("Welcome to Product Price Tracker")


# defining validations for each input
# Checking if a product name is entered or not
def validate_product_name(product_name):
    try:
        if product_name.strip() == "":
            raise ValueError("Empty Product name")
        return product_name
    except Exception as e:
        print("[Error] Invalid product name:", e)
        return None


def validate_product_price(price):
    # This function validates the product price
    try:
        product_price = float(price)
        if product_price <= 0:
            raise ValueError("Price must be greater than 0")
        return product_price
    except Exception as e:
        print("[Error] Invalid Product price:", e)
        return None


def validate_currency(currency):
    # this function checks if the currency is one of USD/EUR/INR/NTD
    try:
        if currency not in ["USD", "NTD", "INR", "EUR"]:
            raise ValueError("Unsupported Currency")
        return currency
    except ValueError:
        print("[Error] Invalid currency! Currency must be one of USD/EUR/INR/NTD")


def main():
    collected_products = []
    while True:

        print("\n" + "=" * 80)
        # check the user input
        text = input(
            f"\nPress Enter to enter details for product or type 'quit' to exit"
        )
        if text.lower() == "quit":
            break
        # capture inputs and validate them with function calls
        product_name = validate_product_name(input("Product Name: "))
        price = validate_product_price((input("Product Price: ")))
        currency = validate_currency(input("Currency (e.g., USD, EUR, NTD): "))

        # store the values after validation if the fields are not empty
        if product_name and price and currency:
            product = {
                "Product Name": product_name,
                "Current Price": price,
                "Currency": currency,
            }
            collected_products.append(product)
    # display the collected data
    if collected_products != []:

        print("========= Product Details ======")
        for i, product in enumerate(collected_products, start=1):
            print(
                f"Product{i}:\n Product Name: {product['Product Name']}\n Current Price: {product['Current Price']} \n Currency: {product['Currency']}"
            )


if __name__ == "__main__":
    main()
