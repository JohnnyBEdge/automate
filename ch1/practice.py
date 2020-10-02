# this program says hello and asks for user name

# print('Hello')
# print('What is your name?')
# userName=input()
# print(f"Nice to meet you {userName}!")

#test whether an input is a string or number
# print("Enter a number")
# strOrNum = input()
# print(type(strOrNum))
# #input returns type string even if number is collected
# # int() changes string to number
# # str() changes argument to string
# # float() changes arg to float
# strOrNum=int(strOrNum)
# print(type(strOrNum))
# print(strOrNum)

# strOrNum=float(strOrNum)
# print(type(strOrNum))
# print(strOrNum)

# strOrNum=str(strOrNum)
# print(type(strOrNum))
# print(strOrNum)

# this will cause an error because it cannot concat a num with a str
# print('I have eaten ' + 99 + ' burritos.')

#this is better
print('I have eaten ' + str(99) + ' burritos.')