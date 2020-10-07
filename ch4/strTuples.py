#MUTABLE AND IMMUTABLE DATA TYPES
# A list value is a mutable data type: It can have values added, removed, or changed. 
# However, a string is immutable: It cannot be changed.

# name = 'john'
# print(name[0]) #j
# name[0] = "J" # throws error
# print(name) 

##TUPLES
# Tuples are just like lists, but written with parentheses
# tup = ('john', 32.95, 'married')
# tup[0] # john
# tup[0:] # john, 32.95, married

# ##BUT THE DIFFERENCE IS THAT TUPLES ARE IMMUTABLE
# tup[0] = 'sarah' #throws error
# print(tup[0])

# if you only have one value in your tuple, follow it with a comma or py will interpret 
# it as a value
# print(type(('hello')))  #str
# print(type(('hello',))) # tuple

# ## USE TUPLES TO INDICATE THIS PIECE OF CODE SHOULDNT CHANGE
# ## Python can implement some optimizations that make code using
# #  tuples slightly faster than code using lists.

# #Just like how str(42) will return '42', the string representation of the inte- ger 42, 
# # the functions list() and tuple() will return list and tuple versions
# #of the values passed to them. 

# tuple(['cat', 'dog', 5]) ('cat', 'dog', 5)
# list(('cat', 'dog', 5)) ['cat', 'dog', 5]
# list('hello')
# ['h', 'e', 'l', 'l', 'o']

# When you assign a list to a variable, you are actually assigning a list reference to the variable. 
# A reference is a value that points to some bit of data, and a list reference is a value that 
# points to a list. 
# test1 = [1,2,3,4,5]
# test2 = test1
# print(test2[0]) #1
# test2[0] = 'one'
# print(test1)
# print(test2)

##COPY AND DEEP COPY
# import copy
# nums = [1,2,3,4,5]
# moreNums = copy.copy(nums)
# moreNums[0] = 'one'
# print(nums) #1,2,3,4,5
# print(moreNums) #'one',2,3,4,5

#If the list you need to copy contains lists, then use the copy.deepcopy() function instead 
# of copy.copy(). The deepcopy() function will copy these inner lists as well.

import copy

lists = [[1,2,3],[4,5,6]]
listcopy = copy.deepcopy(lists)
print(listcopy)