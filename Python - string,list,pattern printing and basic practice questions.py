# ------------------------------------------------------------------------------------------------
# 1. Factorial of a given number.
# -------------------------------------------------------------------------------------------------
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial(5))

# ------------------------------------------------------------------------------------------------
# 2. Given number is prime or not.
# --------------------------------------------------------------------------------------------------
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))

# ----------------------------------------------------------------------------------------------------
# 3. Fibonacci series
# -------------------------------------------------------------------------------------------------
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
fibonacci(6)

# --------------------------------------------------------------------------------------------------
# 4. Palindrome
# ------------------------------------------------------------------------------------------------
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))

# --------------------------------------------------------------------------------------------
# 5. Sum of digits
# -------------------------------------------------------------------------------------------
def sum_digits(n):
    return sum(int(d) for d in str(n))
print(sum_digits(123))

# -------------------------------------------------------------------------------------------------
# 6. Print the alternative values in the given input string.
# --------------------------------------------------------------------------------------------------
def alternate_chars(s):
    return s[::2]
print(alternate_chars("abcdef"))

# ---------------------------------------------------------------------------------------------------
# 7. Get 2 string lists as input. Concatenate values from both string lists
# and print the output in the form of a list.
# ---------------------------------------------------------------------------------------------------
def combine_lists(list1, list2):
    return [a + b for a, b in zip(list1, list2)]
print(combine_lists(["a", "b"], ["x", "y"]))

# --------------------------------------------------------------------------------------------------
# 8. Accessing the list of elements using the given list of indices
#----------------------------------------------------------------------------------------------------
def access_by_indices(data, indices):
    return [data[i] for i in indices]
print(access_by_indices(['a','b','c','d'], [0,2]))

# --------------------------------------------------------------------------------------------------
# 9. Write a Python program to find the largest and smallest elements in a list.
# -------------------------------------------------------------------------------------------------
def min_max(lst):
    return min(lst), max(lst)
print(min_max([3, 1, 7, 5]))

# -------------------------------------------------------------------------------------------------------
# 10. Write a Python program to sort a list of numbers in ascending
# and descending order using sort() method and sorted() method.
# ------------------------------------------------------------------------------------------------------
lst = [5, 2, 9, 1]
print(sorted(lst))
print(sorted(lst, reverse=True))

# ---------------------------------------------------------------------------------------------------
# 11. Write a function that takes a list of words and returns the count of vowels in each word.
# --------------------------------------------------------------------------------------------------
def count_vowels(words):
    vowels = 'aeiouAEIOU'
    return [sum(1 for ch in word if ch in vowels) for word in words]
print(count_vowels(["apple", "sky"]))

# ---------------------------------------------------------------------------------------------------
# 12. Write a python function that takes a list and an element as input
# and returns the count of that element in the list.
# --------------------------------------------------------------------------------------------------
def count_element(lst, elem):
    return lst.count(elem)
print(count_element([1,2,2,3], 2))

# ------------------------------------------------------------------------------------------------------
# 13. Write a python program to find N largest element from the given list of integers.
# ---------------------------------------------------------------------------------------------------
def n_largest(lst, n):
    return sorted(lst, reverse=True)[:n]
print(n_largest([4,1,7,3], 2))

# -------------------------------------------------------------------------------------------------------
# 14. Write a python program to insert an element after sorting the input list such that the
# inserted element does not affect the sorting.
# --------------------------------------------------------------------------------------------------------
def insert_sorted(lst, elem):
    lst.append(elem)
    return sorted(lst)
print(insert_sorted([1,3,5], 4))

# -------------------------------------------------------------------------------------------------------
# 15. Write a python program to compute the cubes of given ‘n’ integers using list comprehension.
# -------------------------------------------------------------------------------------------------------
def cube_list(lst):
    return [x**3 for x in lst]
print(cube_list([1,2,3]))

# ------------------------------------------------------------------------------------------------------
# 16. Write a python program to print the following pattern:
# a) Left-Aligned Triangle Pattern
# *
# * *
# * * *
# * * * *
# ---------------------------------------------------------------------------------------------------------
rows = 4
for i in range(1, rows + 1):
    print("* " * i)

# -------------------------------------------------------------------------------------------------------------
# b) Right-Aligned Triangle Pattern
#   *
#  * *
# * * *
#* * * *
# --------------------------------------------------------------------------------------------------------------
rows = 4
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# --------------------------------------------------------------------------------------------------------------
# 17. Write a python program to print the following pattern:
# * * * *
#  * * *
#  * *
#  *
# ----------------------------------------------------------------------------------------------------------------
rows = 4
for i in range(rows, 0, -1):
    print("* " * i)

# -----------------------------------------------------------------------------------------------------------
# 18. Write a python program to print the following pattern:
# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *
# ---------------------------------------------------------------------------------------------------------------
rows = 7
# Top half
for i in range(1, rows + 1):
    print("*" * i)
# Bottom half
for i in range(rows - 1, 0, -1):
    print("*" * i)

# --------------------------------------------------------------------------------------------------------------
# 19. Given 2 tuples, concatenate them, remove duplicates and sort them.
# -------------------------------------------------------------------------------------------------------------
def process_tuples(t1, t2):
    return tuple(sorted(set(t1 + t2)))
print(process_tuples((1,2,3), (2,3,4)))

# ------------------------------------------------------------------------------------------------------------
# 20. Write a function in Python that accepts a credit card number. It should return a string
# where all the characters are hidden with an asterisk except the last four. For example, if the
# function gets sent “4444444444444444”, then it should return “************4444”.
# --------------------------------------------------------------------------------------------------------------
def mask_card(card):
    return '*' * (len(card)-4) + card[-4:]
print(mask_card("4444444444444444"))


#                                     ----------------X---------------