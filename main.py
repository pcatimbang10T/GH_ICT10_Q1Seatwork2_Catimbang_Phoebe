# main.py

# Variables
restaurant_name = "Phoebe's Pizza Palace"   # string
owner_name = "Phoebe Catombang"             # string
year_established = 2020                     # number
popular_item_price = 8.99                   # number
has_delivery = True                         # boolean
product_names = ["Pepperoni Pizza", "Cheese Pizza", "Hawaiian Pizza"]  # list
business_hours = "Mon-Sun: 10AM - 10PM"     # string
menu_prices = {                             # dictionary
    "Pepperoni Pizza": 8.99,
    "Cheese Pizza": 7.99,
    "Hawaiian Pizza": 9.50
}
common_allergens = ["Dairy", "Gluten", "Soy"]  # list
tax_rate = 0.08                             # number

# Function to display restaurant info
def main():
    print("Welcome to", restaurant_name)
    print("Owner:", owner_name)
    print("Year Established:", year_established)
    print("Popular Item Price: $", popular_item_price)
    print("Delivery Available:", "Yes" if has_delivery else "No")
    print("Business Hours:", business_hours)
    print("Menu:")
    for item, price in menu_prices.items():
        print(f"  {item} - ${price}")
    print("Common Allergens:", ", ".join(common_allergens))
    print("Tax Rate:", tax_rate * 100, "%")

# Run the main function
if __name__ == "__main__":
    main()
