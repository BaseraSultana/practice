# problem 1: Looks fine, right? Now try: print(average([]))
# def average(numbers):
#     total = 0

#     for number in numbers:
#         total += number

#     return total / len(numbers)


# numbers = [10, 20, 30, 40]
# print("Average:", average(numbers))

#                                   solutionnnnnnnn:
# def average(numbers):
#     total = 0
#     if not numbers:
#         print("Input not provided!")
#         return
#     for number in numbers:
#         total += number

#     return total / len(numbers)


# numbers = [10, 20, 30, 40]
# print("Average:", average([]))


# problem 2: The programmer intended to apply a 10% discount.Find the bug.
# cart = {
#     "apple": 50,
#     "banana": 30,
#     "milk": 60
# }

# total = 0

# for item in cart:
#     total += cart[item]

# print("Total:", total)

# discount = 10
# total = total - discount / 100

# print("Final:", total)

#                        solutionnnnnn:
# cart = {
#     "apple": 50,
#     "banana": 30,
#     "milk": 60
# }

# total = 0

# for item, price in cart.items():
#     total += price

# print("Total:", total)

# discount = 10
# total = total * (1 - discount / 100)

# print("Final:", total)


# problem 3: The requirements are:
# - At least 8 characters
# - Contains a letter
# - Contains a number
# Why doesn't the program correctly enforce those requirements?
# password = input("Enter password: ")

# if len(password) < 8:
#     print("Password is too short")
# elif password.isdigit():
#     print("Password is valid")
# elif password.isalpha():
#     print("Password is valid")
# else:
#     print("Password is invalid")

#                                      solutionnnnnn:
password = input("Enter password: ")

if len(password) < 8:
    print("Password is too short")
elif not any(character.isalpha() for character in password) or not any(character.isdigit() for character in password):
    print("Password must contain a letter and a number")

else:
    print("Password is valid")
