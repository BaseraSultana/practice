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

# FREQUENCY COUNTER
# text = "banana"
# count = {}

# for char in text:
#     count[char] = count.get(char, 0) + 1

# print(count)

# PALINDROME
# def is_palindrome(text):
#     if text[::-1] == text:
#         return True
#     else:
#         return False
#     return True


# print(is_palindrome("madam"))

# FIZZ BUZZ
# for i in range(1, 101):
#     if i % 3 and i % 5 == 0:
#         print("FIZZBUZZ")
#     elif i % 3 == 0:
#         print("FIZZ")
#     elif i % 5 == 0:
#         print("BUZZ")
#     else:
#         print(i)

# TWO SUM

# def two_sum(numbers, target):
#     pairs = []
#     for first_index in range(len(numbers)):
#         for second_index in range(first_index + 1, len(numbers)):
#             if numbers[first_index] + numbers[second_index] == target:
#                 pairs.append([first_index, second_index])

#     return pairs


# print(two_sum([2, 7, 11, 6, 5, 4, 15, 3], 9))

# MOVE ZEROS TO THE END
# def move_zeroes(numbers):
#     # numbers = [0, 1, 0, 3, 12]
#     new = []
#     zeroes = []
#     for num in numbers:
#         if num != 0:
#             new.append(num)
#         if num == 0:
#             zeroes.append(num)

#     print(new+zeroes)


# move_zeroes([0, 1, 0, 3, 12])

# FIND THE MISSING NUMBER
# def missing_num(numbers):
#     diff1 = numbers[1]-numbers[0]
#     diff2 = numbers[len(numbers)-1] - numbers[len(numbers)-2]
#     diff3 = numbers[len(numbers)-3] - numbers[len(numbers)-4]
#     # diff4 = numbers[len(numbers)-2] - numbers[len(numbers)-3]
#     if diff1 == diff2:
#         diff1 = diff2
#     elif diff2 == diff3:
#         diff1 = diff2
#     elif diff3 == diff1:
#         diff1 = diff3
#     # elif diff2 == diff4:
#     #     diff1 = diff4

#     for num in range(numbers[0], numbers[len(numbers)-1]+1, diff1):
#         if num not in numbers:
#             print(num)


# missing_num([3, 5, 7, 9, 13])
