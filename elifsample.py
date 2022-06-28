#if elif else flow control

#just playing around with variables and loops
#this will be a robot order taker

print("Hello, welcome to our cafe!")

name = input("What is your name?\n")

#greet them with their name and thank them for coming in using concatenatioin

if name == "Ben":
    freefood_status = input("Are you looking for a free food?\n")
    
#nested if
    if freefood_status == "Yes":
        print("You're not welcome here Ben! Time to leave.")
        exit()
    else:
        print("Oh, well then, come on in.")
else:
    print("Nice to meet you " + name + ", thanks for coming in today.\n")

#menu specials
specials = "tomato soup, grilled cheese, greens, and a blt"

print(name + ", our specials for the day are " + specials + ".")

#ask them what they want to order
order = input("What would you like to order?\n\n")

#Set the price for items
#there has to be a way to clean this up
#is there a way to return all combinations effectivly and without the "and" even if the user types it in
if order == "tomato soup":
    cost = 6
elif order == "grilled cheese":
    cost = 9
elif order == "greens":
    cost = 6
elif order == "blt":
    cost = 9
elif order == "grilled cheese and greens":
    cost = 15
elif order == "grilled cheese and tomato soup":
    cost = 15
elif order == "grilled cheese" + "blt":
    cost = 18
elif order == "tomato soup" and "greens":
    cost = 12
elif order == "tomato soup" and "blt":
    cost = 15
elif order == "greens" and "blt":
    cost = 15
else:
    print("Uh oh, we don't have that item")
    exit()

#find out how many they want
#quantity = input("How many would you like?\n\n")

#total = (cost * int(quantity))

print("Sounds great " + name + ", your price for that will be $" + str(cost) + ".")

print("Great! Your " + order + " will be ready shortly!")
