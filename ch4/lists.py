# ## the list is py's equivolent of JS's array, also with a 0 base index

# ## SLICE
# spam = [1,2,3,4,5]
# print(spam[0]) ## 1
# ## this is a slice, returns a portion of the list, starting with the first int and ends with the second,
# ## but does not include the second. Seperated with a colon
# print(spam[0:3]) ## 1,2,3

# print(spam[:3] == spam[0:3])
# print(spam[0:] == spam[0:5])
# print(spam[:] == spam) 

# ## GETTING THE LENGTH
# ## uses len()
# print(len(spam))

# ## REMOVING VALUES
# ## use 'del'

# del spam[0] ## deletes 1
# print(spam) ## 2,3,4,5

# pizzaToppings=[]
# while True:
#     print(f"Enter one at a time the toppings you would like. To stop, enter nothing.")
#     topping=input()
#     if topping == '':
#         break
#     else:
#         pizzaToppings = pizzaToppings + [topping]
# print(f"Your pizza will have:")
# for i in pizzaToppings:
#     print(i)

##You can determine whether a value is or isn’t in a list with the in and not in operators.
# print('howdy' in ['hi', 'hello', 'hey', 'howdy']) #True
# print('sup' in ['hi', 'hello', 'hey', 'howdy']) #False
# print('hiya' not in ['hi', 'hello', 'hey', 'howdy']) #True
# print('hi' not in ['hi', 'hello', 'hey', 'howdy']) #False

# myPets = ['Zophie', 'Pooka', 'Fat-tail'] 
# print('Enter a pet name:')
# name = input()
# if name not in myPets:
#     print(f'I do not have a pet named {name}') 
# else:
#     print(f'{name} is my pet.')

## MULTIPLE ASSIGNMENTS
## Instead of:
# cat = ['jo',12,'brown']
# name=cat[0]
# age=cat[1]
# color=cat[2]

##you can write:
# name,age,color = cat
##Number of variables and length of the list must be the same for it to work

# APPEND AND INSERT AND REMOVE
# methods to add values to a list

# nums = [1,2,3,4]
# nums.append(5) ## adds to the back of the list
# print(nums)

# nums.insert(1,1.5) ## inserts number at specified index (first arg)
# print(nums)

# nums.remove(1.5) ## removes specified from list
# print(nums)

#SORT
# sort() uses “ASCIIbetical order” rather than actual alphabetical order for sorting strings. 
# This means uppercase letters come before lower- case letters. 
# Therefore, the lowercase a is sorted so that it comes after the uppercase Z.

# abc = ['alex', 'Alex', 'Zach', 'pete']
# abc.sort()
# print(abc)

# # If you need to sort the values in regular alphabetical order, pass str. lower for the key 
# # keyword argument in the sort() method call.

# abc.sort(key=str.lower)
# print(abc)

import random
messages = ['It is certain','It is decidedly so','Yes definitely','Reply hazy try again','Ask again later', 'Concentrate and ask again', 'My reply is no','Outlook not so good', 'Very doubtful']

print(messages[random.randint(0,len(messages)-1)])