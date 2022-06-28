#notes from python training
#dictionaries
ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
for key in ages:
    print(key)
#conditionals in loops   
    
#keys and values tuples
for key, value in ages.items():
    print(key, value)
    
#string
for letter in 'my_string':
    print(letter)
    
#while loop
counter = 1
while counter <= 25: 
    if counter % 4 == 0:
        print(counter)
    counter +=1
    
#continue and break statements
count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue 
#fstring
    print(f"We're counting odd numbers: {count}")
    count += 1
#calling count, then +1, then put the output value into count
    
#break statement
count = 1
while count < 10:
    if count % 2 == 0:
        break
#break stops the execution
    print(f"We're counting odd numbers: {count}")
    count += 1
    
#continue and break statements
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    print(color)
    
#while else
count = 1
while count <= 4:
    print(count)
    count += 1
else:
    print("While loop completed")
    
#for loop
for i in [1, 2, 3, 4, 5]:
    print(i)
else:
    print("For loop completed")
    
#search a collection
colors = ['red', 'pink', 'blue', 'orange', 'green']
for color in colors:
    if color == 'orange':
        print('Orange is in the list')
        break
else:
    print('Orange is not in the list')
    
#iterate a certain number of times, range function
my_range = range(10)
print
#list range
print(list(my_range))

#full range
print(list(range(1, 14, 2)))

count = 1
while count <= 4:
    print('looping')
    count += 1
    
#using for loop
for _ in range(4):
    print('looping')
    
#take a list and go through each item, make modification, list modifications
#list comprehentions
colors = ['red', 'blue', 'orange', 'green', 'yellow']
uppercase_colors = []
for color in colors:
    uppercase_colors.append(color.upper())
print(uppercase_colors)

#list of info but want to put a for loop in - one line
colors = ['red', 'blue', 'orange', 'green', 'yellow']
uppercase_colors = [color.upper() for color in colors]
print(uppercase_colors)

#filering
warm_colors = []
for color in colors:
    if color in ['red', 'orange', 'yellow']:
        warm_colors.append(color)
        print(warm_colors)

#shorter version
colors = ['red', 'blue', 'orange', 'green', 'yellow']
warm_colors = [color for color in colors if color in ['red', 'orange', 'yellow']]
print(warm_colors)

#next up fizz buzz, see fizz buzz file