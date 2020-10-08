# # A diction is Python's equivolent of JS's object

# dog = {'name':'Jazz','age': 3.5, 'colors': ['brown','black']}

# #you can access the keys' values via:
# print(dog['colors'])
# # to add a ket to a dictionary
# dog['weight'] = 45
# print(dog)

# # keys() values() items()
# # return list like view, but these cannot be modified, dont have append method
# dog = {'name':'Jazz','age': 3.5, 'colors': ['brown','black']}
# print(dog.keys())
# print(dog.values())
# print(dog.items())
# # these can be used in for loops, will be returned as tuples
# for i in dog.items():
#     print(i)
# #if you want it to return a true list, use the list keyword
# print(list(dog.values()))


# #checking if a key/value exists in a dict
# person = {'name':'john','age':33,'learning':True}
# #checking for key
# print('name' in person)
# print('name' in person.keys())
# #checking for value
# print('john' in person.values()) 
# print('jabroni' in person.values()) 


# # GET METHOD
# # get takes two values, they key of value to be retrieved and fallback value if it doesnt exist
# cart = {'apple':4, 'cheese': 'gouda', "crackers": 1}
# print(f"oranges: {cart.get('orange',0)}")
# print(f"apples: {cart.get('apple',0)}")


# # SETDEFAULT METHOD
# # takes 2 args: one to check, second to set to if it doesnt exist
# colors={'black':True,'green':True}
# colors.setdefault('red',False)
# print(colors)
# colors.setdefault('red',True) #doesnt change red because it already exists
# print(colors)

# #count the number of each letter in a sentence
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count={}
# for char in message:
#     #checks if character exists in count, if not adds it with starting key of 0
#     count.setdefault(char,0)
#     #updates count now that it has been added to count
#     count[char] = count[char] + 1
# print(count)

# #PRETTY PRINTING
# #importing pprint gives you access to pprint() and pformat()
# #these give you a cleaner display of items in a dict
# import pprint
# pprint.pprint(count)


