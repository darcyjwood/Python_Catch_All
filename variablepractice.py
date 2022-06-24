#just playing around with variables
#this will be a robot order taker

print("Hello, welcome to our cafe!")

name = input("What is your name?\n")

print("Nice to meet you " + name + ", thanks for coming in today.\n")

specials = "tomato soup, grilled cheese, greens, and a BLT"

print(name + ", our specials for the day are " + specials + ".")

order = input("What would you like to order?\n\n")

cost = 12

quantity = input("How many would you like?\n\n")

total = (cost * int(quantity))

print("Sounds great " + name + ", your price for that will be $" + str(total))

print("Great! Your " + order + " will be ready shortly!")