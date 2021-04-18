__author__ = "Rhiannon Hoyte"
"""This is a program that will tell you how many items you bought ,the total
# amount of money you spent ,and how much money you have left over after
# shopping."""
# Sources POGIL , w3schools, and Professor Vanselow
import math
print("Hello", "welcome to shopping assistant", sep="! ")
print("What is your name?")
name = input("Enter your name: ")
print("Hello", name + "!\nwelcome ")
print("How much money do you have to spend?")
# Enter the total amount of money you have to spend example 20.00
money = float(input("Enter amount of money: "))
print("How many items are you purchasing today?")
item_names = []
name = 0
count = 0
total_items = int(input("Enter total number of items: "))
print("What are the names of your items? ")
# The program will ask for total amount of items then ask the user to input
# the name of each item everytime a name is input the program will save it
# to a list called item_names in the end the list is sorted alphabetically
while count < total_items:
    name = input("Enter the name of the item: ")
    item_names.append(name)
    count = len(item_names)
    item_names.sort()

# The program will ask if the list of items is correct and give the user the
# option to input yes or no if they input no the program will give the
# option to delete items from the list if they say yes the program will move
# on to determine the prices of items if neither yes or no is input then the
# program will print an error message


def shopping_list():
    count_2 = 0
    print("Is this shopping list correct? ")
    for i in item_names:
        print(i)
    response = input("Enter yes or no: ")
    if response == "no":
        print("Would you like to delete an item? ")
        response_2 = input("Enter yes or no: ")
        if response_2 == "yes":
            print("How many items would you like to delete? ")
            delete_total = int(input("Enter the total number of items you "
                                     "would like to delete: "))
            while count_2 < delete_total:
                count_2 = count_2 + 1
                print("What would you like to delete from the list? ")
                item_delete = str(input("Enter the item you would like "
                                        "to delete:"))
                item_names.remove(item_delete)
                print("item", item_delete, "has been deleted")
    elif response == "yes":
        print("Excellent!")
        print("What is the cost of all of your items? ")
    else:

        print("Error please enter yes or no")
        print(input("Enter yes or no: "))


shopping_list()
total_items = len(item_names)
item_prices = []
total_cost = 0
price = 0
x = 0
# This part of the program will determine prices of each item previously
# listed the program will list each item from the item_names list and ask
# the user to input the price every time the user inputs a price it will be
# added a list called item_prices
while x < len(item_names):
    print(item_names[x])
    x = x + 1
    price = float(input("Enter the price of the item: "))
    item_prices.append(price)
    count2 = len(item_prices)
# the zip function was used to combine item_names list and item_prices list
# and the dict function was used to turn the combined lists into a
# dictionary named shopping_receipt then it is printed line by line
shopping_receipt = dict(zip(item_names, item_prices))
for x in shopping_receipt:
    print(x, ':', shopping_receipt[x])
# This part of the program uses a while look to calculate the total price of
# all the combined items including tax and calculates the savings
total_cost = sum(item_prices)
total_amount = 0
savings = 0
while total_amount == 0:
    tax_rate = 0.06
    amount_of_tax = total_cost * tax_rate
    total_amount = total_cost + amount_of_tax / 1
    savings = money - total_amount
# total_items was a float and could not be used in range so I turned it into
# an integer
# and assigned it to variable total_items2
total_items2 = math.floor(total_items ** 2 // total_items)
# Prints item number and the cost of each item the user input in the form of
# a list
print("Congratulations!" * 2)
# Tells you how many items you bought in total
print("You bought a total of", total_items2, "items")
# Tells you if you spent an even amount if not it gives you your normal total
if not (total_amount % 2 != 0):
    print("You have spent a total of", "$" + format(total_amount, '.2f'),
          "even")
else:
    print("You spent a total of", "$" + format(total_amount, '.2f'))
# If your total amount is more than the money you have to spend
# the program tells you you don't have anymore money to spend
if (total_amount == money) or (total_amount > money):
    print("Sorry! You have no more money left")
# Tells you how much money you have left over if your total is less than the
# amount of money you have to spend
elif (total_amount != money) and (total_amount < money):
    print("After spending", "$" + format(total_amount, '.2f'), "you have",
          "$" + format(savings, '.2f'), "left over")
print("Thank you for using shopping assistant", "Good" + "bye", end='.')
