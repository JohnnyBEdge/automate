##if else elif practice
# name=input("What is your name?")
# if name == "john":
#     print(f"welcome back {name}")
# elif name != "john":
#     print(f"I dont know any {name}s")
#     age = input("how old are you?")
#     if int(age) > 18:
#         print(f"Please sign in")
#     else:
#         print(f"You are too young, go home {name}")

## while loops
# age = 1
# while int(age) < 18:
#     print(f"{age} is too young. Come back in one year")
#     age +=1
# print(f"you are now {age}, welcome")

## breaks, continues, if/else and loops
# while True:
#     print("What is your name?")
#     name=input()
#     if name != "John":
#         #if name is not john, continue jumps to the top of the loop
#         continue
#     print(f"Hello {name}. What is the password?")
#     password = input()
#     if password == "swordfish":
#         #if the correct pwd, break ends the loop
#         break
# print("access granted")

## For/Range
# print('My name is') 
# for i in range(5):
#     print('Jimmy Five Times (' + str(i) + ')')

# total = 0
# for num in range(101):
#     total = total + num
# print(total)

for i in range(0,100,5):
    print(i)