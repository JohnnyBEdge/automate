import random

def magic8(num):
    if num == 1:
        return 'It is certain'
    elif num == 2:
        return 'It is decidedly so'
    elif num == 3:
        return 'Concentrate and ask again'
    elif num == 4: 
        return 'My reply is no'
    elif num == 5:
        return 'Very doubtful'

r = random.randint(1,5)
fortune = magic8(r)
print(fortune)

# None value
# None reps an absence of a value
# it is the only value of the NoneType data value
# must be capitalized
# useful when you need to store something that wont be confused with a real value in a variable
# 
print('dogs','cats','mice')
print('dogs','cats','mice', sep=',')

# print automatically puts items on a new line as it ends with (you dont see it) \n
# using the end arugument will replace \n, cause print statements to be on the same line
print('hello')
print('world')
print('hello', end=' ')
print('world')

# GLOBAL STATEMENT
# if you need to modify a global variable from within a function, use the global statement
# bc eggs is declared at the top of spam, when eggs is set to 'spam', this assignment is done
# to the globally scoped eggs
# If there is a global statement for that variable in a function, it is a global variable.
def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)

def spam():
    global eggs
    eggs = 'spam' #this is the global
def bacon():
    eggs = 'bacon' # this is a local
def ham():
    print(eggs) # this is the global
eggs = 42 # this is the global
spam()
print(eggs)