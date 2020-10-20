#escape characters
# \' for a single quote
# \" for a double quote
# \t Tab
# \n new line/line break
# \\ backslash

#multiline strings
# print('''multiline strings
# use the triple single quotes.
# Indent rules do no apply''')

#isX() methods, returns booleans
# isalpha() ret True is str consist only ofletters and isnt blank
# isalnum() ret True is str consists only of letters and nums and not blank
# isdecimal() ret True if string ocnsists only of numeric char and not blank
# isspace() ret True if str consists only of spaces tabs and newlines and not blank
# istitle() ret True if str consists only of words that begin w uppercase letter followed by lowercase
# print('hello'.isalpha() )
# print('hello123'.isalpha())
# print('hello123'.isalnum())
# print('hello'.isalnum())
# print('123'.isdecimal())
# print(' '.isspace())
# print('This Is Title Case'.istitle())
# print('This Is Title Case 123'.istitle())
# print('This IS NOT Title Case'.istitle())
# print('This IS Not Title Case either'.istitle())

#this are helpful to validate user input
# while True:
#     print('Enter your age')
#     age = input()
#     if age.isdecimal():
#         break
#     print(f'{age} is not a number.')

# while True: 
#     print('Create a new password consisting of only numbers and letters.')
#     pwd = input()
#     if pwd.isalnum():
#         break
#     print(f'Passwords can only have letters and numbers')

# startswith() and endswith() methods
# returns True if str they are called on begins or ends with the passed str
# print('Hello there cruel world'.endswith('world'))
# print('Hello there cruel world'.startswith('world'))

# partition() method
# can split a str into the text before and after a seperator string
#returns a tuple
# print('Hello, world!'.partition('w')) # // ('Hello, ', ' w', 'world')
# # if the passed str occurs multiple times, it only occurs on the first occurance
# print('Hello, world'.partition('o')) # //('Hell', 'o', ', world')
# #if passed str not found:
# print('Hello, world'.partition('XYZ')) # // ('Hello, world', '', '')
# You can use the multiple assignment trick to assign the three 
# returned strings to three variables:
# before, sep, after = 'hello, world!'.partition(' ')
# print(before)
# print(sep)
# print(after)

#removing whitespace
# spam='   Hello, World  '
# print(spam.strip()) # removes white space from both ends
# print(spam.lstrip()) # removes white space from left side
# print(spam.rstrip()) # removes white space from right side
# print(spam.strip('World  ')) 

#numeric values of chars with ord() and chr()
# each str char has a numeric representation called Unicode code point
print(ord('A'))
print(ord('B'))
print(ord('a'))
print(ord(' '))
print(ord('!'))

print(ord('A') < ord('B'))
