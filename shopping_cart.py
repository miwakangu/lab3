"""
Author: Ian Wakangu Mwangi
Date: 2025-05-23
This program simulates a simple shopping cart.
Users can add items, specify quantities, and see the total cost.
The program uses exception handling to manage invalid inputs.
"""
print("Welcome to the Shopping Cart Program!")

item_number = 0
try:
    item_number = int(input("Enter the number of items you are buying: "))
    """ we will use the item_number as a counter so as to tell the program how
        many times to ask the user for his goods and their amount
    """

except ValueError:
    print("Invalid input. Please enter a whole number.")
    #This exception handling will prompt the user to enter a whole number


item_total_cost = 0     #variable for total cost of each item
total_cost = 0          #variable for total cost of all the goods

while item_number > 0:  #while loop for collecting name of goods, prices & total cost
    item_number -= 1 # the counter will minus 1 until the number is 1 (
    item_name =input("Enter the name of the item: ")

    try:
        item_price = float(input("Enter the price of the item: "))
        item_quantity = int(input("Enter the quantity of the item: "))
        item_total_cost = item_price * item_quantity
        total_cost += item_total_cost

    except ValueError:
        print("Invalid input. Please enter valid numbers")

    """ If the user enters a value a value of the wrong data type ,
        the program will prompt them to enter a valid input.
    """

if total_cost > 100: #The if statement checks whether the user has
 discount = total_cost * 0.1
 total_cost -= discount

 print(f"\nThe total cost of your goods is {total_cost}")
 print(f"\nYou saved ${discount:.2f} with a 10% discount!")
 print(f"Discounted Total: ${total_cost:.2f}")



"""
The program can now display the discounted price of the bought goods.
"""
