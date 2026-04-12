print("Welcome to Product Price Tracker")

collected_products = []

exit_word = ""
while True:
    i = 0
    print("\n" + "=" * 80)
    print(f"\nEnter details for product {i+1}:")
    name = input("Product Name: ")
    price = float(input("Product Price: "))
    currency = input("Currency (e.g., USD, EUR, NTD): ")
    product = {"Product Name": name, "Current Price": price, "Currency": currency}
    collected_products.append(product)
    exit_word = input(
        "Enter done if you finished entering products else press enter to continue"
    )
    if exit_word.lower() == "done":
        break

print("========= Product Details ======")
for i, product in enumerate(collected_products, start=1):
    print(
        f"Product{i}:\n Product Name: {product['Product Name']}\n Current Price: {product['Current Price']} \n Currency: {product['Currency']}"
    )

if len(collected_products) == 3:
    print("You have added 3 products - ready to track their prices!")
elif len(collected_products) > 3:
    print(f"You have added {len(collected_products)} products to the tracking list")
else:
    print(
        f"You have collected {len(collected_products)} products. Missing {3-len(collected_products)} more product to be added."
    )

tw_products = [item for item in collected_products if item["Currency"] in ["NTD"]]


if tw_products:
    print("Taiwan Products on the tracking list are:\n")
    for i, product in enumerate(tw_products, start=1):
        print(
            f"Product{i}:\n Product Name: {product['Product Name']}\n Current Price: {product['Current Price']} \n Currency: {product['Currency']}"
        )
else:
    print("No taiwan products to be tracked!!")
