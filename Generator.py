#
#EC2 Random Name Generator

#import libraries
import random
import string

#creating string of 8 random letters/digits that will follow first 4 letters of employees name.
#x = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)])

#verifying employee is in an approved department (Accounting, Marketing or FinOps)
while True:
    try:
        dept = input("Which department do you work for (Accounting, Marketing, FinOps)? ").lower()
        list = ["accounting", "marketing", "finops"]
        if dept not in list:
            raise ValueError
        break
    except ValueError:
        print("Only Accounting, Marketing and FinOps are allowed to use this programs. Contact your lead for further direction")
        exit ()
    else:
        break
    
#generating the first 4 letters of the unique EC2 instance assigned to employee
while True:
    try:
        name = (input("Enter the first letter of your name and first 3 letters of your last name (ex: Dana Gibson = dgib: "))
        if len(name) != 4:
            raise ValueError
        break
    except ValueError:
        print("Response must be 4 letters, try again.")
        continue
    else:
        break

#identifying the number of unique EC2 names an employee will need
while True:
    try:
        numb = int(input("How many instances do you need? "))
        break
    except ValueError:
        print("Response must be a number value (ie. 2 NOT two), try again.")
        continue
    else:
        break

#creating string of 8 random letters/digits that will follow first 4 letters of employees name.
unique_id = ''.join([random.choice(string.ascii_letters + string.digits) for numb in range(8)])

x = numb

for _ in range(x):
    unique_id = str(''.join([random.choice(string.ascii_letters + string.digits) for numb in range(8)]))
    print('{}-{}'.format(name, unique_id))