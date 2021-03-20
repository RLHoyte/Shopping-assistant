# Rhiannon Hoyte
# This is a program that will tell you how many items you bought ,the total
# amount of money you spent ,and how much money you have left over after shopping.
# Sources POGIL , w3schools, and Professor Vanselow
import math
print("Hello! welcome to shopping assistant")
print("What is your name?")
name = input("Enter your name: ")
print("Hello", name + "!\nwelcome to my program")

print("How much money do you have to spend?")
# Enter the total amount of money you have to spend example 20.00
money = float(input("Enter amount of money: "))
print("How many items are you purchasing today?")
cost_list = []
total_items = float(input("Enter total amount of items: "))
item = 1
total_cost = 0
while item <= total_items:
    cost = float(input("Enter cost of item " + str(item) + " "))
    cost_list.append(cost)
    item += 1
    total_cost = total_cost + cost
    item_list = total_items + 1
    tax_rate = 0.06
    amount_of_tax = total_cost * tax_rate
    total_amount = total_cost + amount_of_tax/1
    savings = money - total_amount


# total_items was a float and could not be used in range so I turned it into an integer
# and assigned it to variable total_items2
total_items2 = math.floor(total_items**2//total_items + 1)

# Prints item number and the cost of each item the user input in the form of a list
numItem = -1
for x in range(1, total_items2):
    numItem += 1
    print("item", x, ":", sep='')
    print(cost_list[numItem], sep='\n')

print("Congratulations!" * 2)
# Tells you how many items you bought in total
print("You bought a total of", total_items2, "items")
# Tells you if you spent an even amount if not it gives you your normal total
if not(total_amount % 2 != 0):
    print("You have spent a total of", "$"+format(total_amount, '.2f'), "even")
else:
    print("You spent a total of", "$"+format(total_amount, '.2f'))
# If your total amount is more than the money you have to spend
# the program tells you you don't have anymore money to spend
if (total_amount == money) or (total_amount > money):
    print("Sorry! You have no more money left")
# Tells you how much money you have left over if your total is less than the amount of money you have to spend
elif (total_amount != money) and (total_amount < money):
    print("After spending", "$"+format(total_amount, '.2f'), "you have", "$"+format(savings, '.2f'), "left over")
print("Thank you for using shopping assistant", "Good" + "bye", end='.')
