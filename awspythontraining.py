#notes from aws python training
#this is just a mess of random notes that can be used as reference later


a_str = "This is an example of a string in quotes" # In python the word string is abbreviated to str
my_float = 5.5
an_integer = 5 # integer is abbreviated to int
shopping_list = ["apples", "oranges", "pears"]
a_dict = {"userId": "JBloggs"} # dictionary is abbreviated to dict
my_var = another_variable # variable is abbreviated to var
test_function = my_function() #function is abbreviated to func
example_tuple = ("apple", "orange", "pear")
boolean_values = True # boolean is abbreviated to bool


"The quick brown fox jumped over the lazy dog"
'The quick brown fox jumped over the lazy dog'
'The error message was "Incorrect DataType"'


>>>first_name = "Monty"
>>>last_name = "Python"

>>>print(first_name+last_name)
MontyPython

>>>print(first_name + " " + last_name)
Monty Python


>>>first_name = "John"
>>>surname = "Doe"
>>>print("My first name is {}. My family name is {}".format(first_name, surname))


firstname = "Jane"
surname = "Doe"

print(f"My first name is {firstname}. My family name is {surname}")


my_int = 50
sentence = "The total comes to: "

print(sentence + my_int)

#to avoid a typeerror
my_int = 50
sentence = "The total comes to: "

print(sentence + str(my_int))

str() returns a string object
int() returns an integer object
float() returns a floating point object
bool() a boolean value of True or False

A dictionary is a way of storing related information in key-value pairs. 
It uses a key as an identifier and a value to store the information. 
For example, the key could be first_name and the value could be Ada.

A dictionary when written in python would look like {"first_name":"Ada"}. 
A dictionary in python is abbreviated to dict and has the following syntax {"key":"value"}. 
The key is a string providing an identifier and the value can be the 
same kind of values you would store in a variable.

#CREATE DICT
>>> user = {"first_name":"Ada"}
>>> print(user)
{'first_name': 'Ada'}

Assigning {} to a variable, for example:

account_details = {}

or use the dict() constructor:

account_details = dict()

#READ DICT
To read the value associated with a key, you need to provide the name of the dictionary 
and the the value of the key inside square brackets.

>>> user = {"first_name":"Ada"}
>>> print(user["first_name"])
Ada

#UPDATE DICT
Dictionaries are mutable, which means they can be changed after you create them. 
You can add, update or delete the key-value pairs in a dictionary.

To add an additional key-value to a dictionary, provide the dictionary name, 
the new key in [] and a value after an = sign.

>>>user["family_name"] = "Byron"
>>>print(user)
{'first_name': 'Ada', 'family_name': 'Byron'}

#MODIFY VALUE
user["family_name"] = "Lovelace"
print(user)
{'first_name': 'Ada', 'family_name': 'Lovelace'}

#DELETE KEY-VALUE PAIR
>>> del user["family_name"]
>>> print(user)
{'first_name': 'Ada'}

#CREATE LIST
>>>fruit = ["apples","oranges","bananas"]
>>>print(fruit[1])
oranges

>>>len(fruit)
3

#UPDATE LIST
Lists are mutable, which means they can be changed after you create them. 
You can add, update, delete and reorder elements in a list.

You can use append() to add an element to the end of the list.

>>> fruit.append("kiwi")
>>> print(fruit)
['apples', 'oranges', 'bananas', 'kiwi']


To add element to specific point - 
>>> fruit.insert(2, "passion fruit")
>>> print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']

#ORGANIZE LIST
>>>print(sorted(fruit))
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']
>>>print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']

In the example above you can see that the sorted() function return a sorted list, 
but does not alter the original order of the list.

If you want to permanently sort the list, you should use the sort() method.

>>> fruit.sort()
>>> print(fruit)
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']

Reverse order

>>>fruit.reverse()
>>> print(fruit)
['passion fruit', 'oranges', 'kiwi', 'bananas', 'apples']


#DELETE ELEMENTS FROM LIST
>>> del fruit[1]
>>> print(fruit)
['passion fruit', 'kiwi', 'bananas', 'apples']

If you want to use the value after removing it from a list you use the pop() method. 
To use pop(), you need to store the value you have removed from the list inside another variable.

>>>favorite_fruit = fruit.pop()
>>>print(favorite_fruit)
apples

>>> fresh_fruit = fruit.pop(1)
>>> print(fresh_fruit)
kiwi


>>> fruit.remove('bananas')
>>> print(fruit)
['passion fruit']
Remember that when you use del, pop() or remove(), the element is permanently deleted from the original list. 
If the list is printed out, you will see that those elements are no longer stored in the list.

#DETERMINING TYPE
to figure out type;

>>>my_variable = "A string"
>>>print(type(my_variable))

<class 'str'>

>>> my_number = 50
>>> some_string = "The number is "
>>> print(some_string + my_number)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

>>> my_number = 50
>>> some_string = "The number is "
>>> print(some_string + str(my_number))
The number is 50

response = client.translate_text(
    Text='string',
    TerminologyNames=[
        'string',
    ],
    SourceLanguageCode='string',
    TargetLanguageCode='string'
)
import boto3

client = boto3.client('translate')

#### Add the new text below this line ####

def translate_text(): # declare the function using def, name, braces for parameters and a colon  
    response = client.translate_text(
        Text='I am learning to code in AWS', # Assigning the value of the string to the variable Text
        SourceLanguageCode='en', # We are using a two letter language code from the documentation (en = English)
        TargetLanguageCode='fr' # We use a second two letter language code from the documentation (fr = French)
    )

import boto3

client = boto3.client('translate')

#### Add the new text below this line ####

def translate_text(): # declare the function using def, name, braces for parameters and a colon  
    response = client.translate_text(
        Text='I am learning to code in AWS', # Assigning the value of the string to the variable Text
        SourceLanguageCode='en', # We are using a two letter language code from the documentation (en = English)
        TargetLanguageCode='fr' # We use a second two letter language code from the documentation (fr = French)
    )


#TRANSLATOR

import boto3

client = boto3.client('translate')

def translate_text(): 
    response = client.translate_text(
        Text='I am learning to code in AWS', 
        SourceLanguageCode='en', 
        TargetLanguageCode='fr' 
    )
#### Add the new text below this line ####
    print(response) # this code is inside the function and will print the contents of the variable 'response' 

translate_text() # This line will call our function. Without it, python will not do anything.


{'TranslatedText': "J'apprends à coder dans AWS", 'SourceLanguageCode': 'en', 'TargetLanguageCode': 'fr', 'ResponseMetadata': {'RequestId': 'db2e2966-000a-4474-97cd-337b6249b783', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'db2e2966-000a-4474-97cd-337b6249b783', 'cache-control': 'no-cache', 'content-type': 'application/x-amz-json-1.1', 'content-length': '101', 'date': 'Fri, 28 Feb 2020 10:14:32 GMT'}, 'RetryAttempts': 0}}


Return type
    dict

Returns
    Response Syntax

    {
        'TranslatedText': 'string',
        'SourceLanguageCode': 'string',
        'TargetLanguageCode': 'string',
        'AppliedTerminologies': [
            {
                'Name': 'string',
                'Terms': [
                    {
                        'SourceText': 'string',
                        'TargetText': 'string'
                    },
                ]
            },
        ]
    }



import boto3

client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text='I am learning to code in AWS',
        SourceLanguageCode='en',
        TargetLanguageCode='fr'
    )
    print(response) # this code is inside the function and will print the contents of the variable 'response'

def main():
    translate_text()

if __name__=="__main__":
    main()
    
    
#Arguments are used to pass values between programs, subroutines or functions. When an argument is used to customize a program, it is called a parameter.



with open(filename, 'r' ) as variable_name:
    <Do something with the variable here>


