# shopping_cart.py

import os 
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
#Discussion with Abhi in Zoom meeting

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output


#Info capture

total_price = 0
selected_ids=[]

while True:
    selected_id = input("Please input a product identifier: ") #string version
    if selected_id == "DONE":
        break
    else:
        selected_ids.append(selected_id)
        #based on Professor Rossetti's Guided Screencast (https://www.youtube.com/watch?v=3BaGb-1cIr0)


#Info output/display


print("TOTAL PRICE: " + str(total_price))

#viewable Aesthetics for program
print("______________")
print("Dairy Barn Grocery")
print("______________")
print("Website: www.dairybarn.com")
print("Phone:(631)427-1420")
print("________________")
now = datetime.now() #https://www.geeksforgeeks.org/get-current-date-and-time-using-python/
print("Current Checkout Time:", now.strftime("%b %d %Y %H:%M:%S %p"))
print("_________________")
print("Selected Products:")

for selected_id in selected_ids:
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0]
        total_price = total_price + matching_product["price"]
        print("..." + matching_product["name"] + " " + to_usd(matching_product["price"]))
        #based on Professor Rossetti's Guided Screencast (https://www.youtube.com/watch?v=3BaGb-1cIr0)

print("__________________")

Tax_var = os.getenv("tax_rate", default = .0875)
taxx = float(Tax_var) * total_price
net_total = total_price + taxx
#Discussion with Abhi in Zoom meeting



print( "Subtotal: " + to_usd(total_price))
print("Tax: " + to_usd(taxx))
print("Total: " + to_usd(net_total))


print("________________")
print("Thank you for shopping today! Come again soon.")
print("________________")


