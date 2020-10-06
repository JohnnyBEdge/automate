## EXCEPTION HANDLING
## Right now, getting an error, or exception, in your Python program means the entire program will 
## crash. You don’t want this to happen in real-world pro- grams. Instead, you want the program to 
## detect errors, handle them, and then continue to run.

# def divideBy(num):
#     return 10 / num
# print(divideBy(5))
# print(divideBy(2))
# print(divideBy(0))
# print(divideBy(1))

def divideBy(num):
    try:
        return 10 / num
    except ZeroDivisionError:
        print("Error: Invalid argument.")
        
print(divideBy(5))
print(divideBy(2))
print(divideBy(0))
print(divideBy(1))