#EC2 Random Name Generator

#welcome user and collect name
print("Hello, welcome to your EC2 Random Name Generator!")
name = input("What is your name?\n")
print(("Thank you. Nice to meet you, ") + (name.capitalize()) + ("."))

#get the users department name
dept = input("What department do you work for? Select one: Accounting, Marketing, or FinOps?\n").upper()

#user needs to be in an approved department
while True:
    try:
        list = ["ACCOUNTING", "MARKETING", "FINOPS"]
        if dept not in list:
            raise ValueError
        break
    except ValueError:
        print("You are not allowed to use the EC2 Random Name Generator.")
        exit()
    else: 
        print("Great, thank you. Let's get started, shall we?")
        
#get the number of unique EC2 names the user wants
while True:
    try:
        instnumb = int(input("How many instance names do you need? "))
        print("Great! We'll get you those " + str(instnumb) + (" random instance names to you right away. Enjoy!"))
        print("Here they are:")
        break
    except ValueError:
        print("Response must be a number value only. Please try again.")
        continue
    else:
        break
    
#random letters and digits that will follow the department name will be generated
import string
import random
n = instnumb
N = 3

for _ in range(n):
    custom_id = str(''.join([random.choice(string.ascii_letters + string.digits) for instnumb in range(10)]))
    print('{}-{}'.format(dept[0 : N], custom_id))
    
print(("Thanks for using the EC2 Random Name Generator, ") + (name.capitalize()) + (". Goodbye."))