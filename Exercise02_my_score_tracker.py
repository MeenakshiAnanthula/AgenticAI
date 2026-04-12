print("Welcome to Product Price Tracker")

collected_products = []

# collecting 3 products from user for which price needs to be tracked
for i in range(3):

    print("\n" + "=" * 80)
    # taking product details through user inputs
    print(f"\nEnter details for product {i+1}:")
    name = input("Product Name: ")
    price = float(input("Product Price: "))
    currency = input("Currency (e.g., USD, EUR, NTD): ")
    # storing the inputs in the form of dictionary
    product = {"Product Name": name, "Current Price": price, "Currency": currency}

    # storing each product by appending it to the list
    collected_products.append(product)

# printing the product details
print("========= Product Details ======")
for i, product in enumerate(collected_products, start=1):
    print(
        f"Product{i}:\n Product Name: {product['Product Name']}\n Current Price: {product['Current Price']} \n Currency: {product['Currency']}"
    )

# checking length of list and printing status message
if len(collected_products) == 3:
    print("You have added 3 products - ready to track their prices!")
elif len(collected_products) > 3:
    print(f"You have added {len(collected_products)} products to the tracking list")
else:
    print(
        f"You have collected {len(collected_products)} products. Missing {3-len(collected_products)} product to be tracked."
    )

# using list comprehension to filter taiwan products
tw_products = [item for item in collected_products if item["Currency"] in ["NTD"]]

# displaying Taiwan products
print("Taiwan Products on the tracking list are:\n")
if tw_products:
    for i, product in enumerate(tw_products, start=1):
        print(
            f"Product{i}:\n Product Name: {product['Product Name']}\n Current Price: {product['Current Price']} \n Currency: {product['Currency']}"
        )
else:
    print("No taiwan products to be tracked!!")
