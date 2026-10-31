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
cart = {
    "apple": 50,
    "banana": 30,
    "milk": 60
}

total = 0

for item in cart:
    total += cart[item]

print("Total:", total)

discount = 10
total = total - discount / 100

print("Final:", total)
