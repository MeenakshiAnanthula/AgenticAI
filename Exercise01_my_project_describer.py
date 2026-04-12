"""Product Price Tracker 🌏 Universal
What it does: Stores product names and prices over time;
shows price trend and alerts when a product hits a target price."""

print("Welcome to My Project Describer")
print("Answer 3 questions about your project")
print()
# taking the inputs to know about the project
product_name = input("Which product price are you going to track?")
current_price = float(input("Whats' the current price of it?"))
target_price = float(input("Whats' the desired price you are looking for?"))
currency = input("In which currency are you tracking?")
dateTimeStamp = input("When was this price recorded?")

# taking inputs to know the domain and motivation
project_domain = input("Which domain is your project focused in?")
purpose = input("What's main motivation of your project?")

# setting the project description with inputs received
project_description = f"""
=============================================================================================
               Description of my project
============================================================================================                
My project tracks the price trend of {product_name} in {currency} and alerts' me 
when it hits the {target_price}. The price recorded on {dateTimeStamp} is {current_price}.

"""
print(project_description)

para2 = f"""

This project is for {project_domain.upper()} and solves the problem of {purpose}.
=============================================================================================
"""
print(para2)
