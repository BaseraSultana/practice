# to find the largest number without max() function.
# numbers = [12, 45, 7, 89, 23, 56]
# largest = numbers[0]
# for i in numbers:
#     if i > largest:
#         largest = i

# print(largest)

# TO FIND THE NUMBER OF EVEN NUMBERS IN THE LIST
# numbers = [2, 7, 10, 13, 18, 21, 24, 31]
# even = []
# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)

# print(len(even))

#  REVERSE STRING
# poo = "python"
# qoo = ""
# i = len(poo) - 1
#     while i >= 0:
#         qoo += poo[i]
#         i -= 1

# print(qoo)
# poo = "python"
# qoo = ""
# i = 0
# while i <= len(poo)-1:
#     qoo += poo[i]
#     i += 1

# print(qoo)

# COUNT THE VOWELS IN A STRING
# def count_vowels(text):
#     even = []
#     for num in text:
#         if num in "aeiou":
#             even.append(num)

#     print(len(even))


# count_vowels("cybersecurity")

# DICTIONARY
# student = {
#     "name": "Basera",
#     "age": 17,
#     "course": "Computer Science"
# }
# print(student.get("name"))
# student["age"] = 18
# # his or that
# # student.update({"age" : 18})
# student.update({"city": "Hyderabad"})
# print(student.items())

# FUNCTION TO CHECK IF A NUMBER IS PRIME
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False

#     # Check odd divisors up to sqrt(n)
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True


# # practice
# # Test the function
# print(is_prime(7))      # True
# print(is_prime(10))     # False
# print(is_prime(2))      # True
# print(is_prime(1))      # False

# REMOVE DUPLICATES WITHOUT USING SETS
# numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
# unique = []
# for i in numbers:
#     if i not in unique:
#         unique.append(i)

# print(unique)

# SECOND LARGEST DISTINCT NUMBER:
# numbers = [10, 25, 7, 40, 32, 40, 15]
# largest = None
# second_largest = None
# for num in numbers:
#     if num == largest:
#         continue

#     if largest is None or num > largest:
#         second_largest = largest
#         largest = num
#     elif second_largest is None or num > second_largest:
#         second_largest = num

# print(second_largest)
# if len(numbers) < 2:
#     print("Not enough elements")
# else:
#     largest = second = numbers[0]

#     for num in numbers:
#         if num > largest:
#             second = largest
#             largest = num
#         elif num > second and num != largest:
#             second = num

#     print(second)
# problem 16 to be started.....
# more problems are to be completed
# revising the previous problems
