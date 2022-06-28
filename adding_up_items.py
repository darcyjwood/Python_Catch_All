# items and their prices
items = {'banana': 3,
         'apple': 2,
         'milk': 12,
         'bread': 15,
         'orange': 3,
         'cheese': 14, 
         'chicken': 42,
         'peanuts':32 ,
         'butter': 20,
         'cooldrink': 18,
         }
#Asking for the item
choice = input("Select your item(type 'nothing' to make it stop) \n : ")
#the list the purchased items would go into
price = []
while items != 'nothing':
    input('Another item?: ')
    if choice in items:
        the_choice = price[choice]
    else:
        print("Uh oh, I don't know about that item")
