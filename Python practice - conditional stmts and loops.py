# --------------------------------------------------------------------------------------------------------------
# 1. if – elif:
# Dinesh started learning Geometry today. He doesn't know the formulae to calculate the areas of
# different shapes. His teacher has just taught him how to calculate the areas of basic shapes
# including square, rectangle, triangle and circle. He is facing the problem to memorise all these
# formulae. Create a python logic to help Dinesh to display the formulae when he selects the shape.

# Hint:
# Area of Square = side^2
# Area of Rectangle= lengthXbreadth
# Area of Triangle = 0.5XbaseXheight
# Area of circle= 3.14Xradius

# Dinesh will enter letters S for Square, R for Rectangle, T for triangle and C for Circle
# Input --- One line of input contains the First alphabet of shape in Capital form.
# Output ----- Formula for corresponding shape.
# Example input ----S
# Output ----side ^2

# Note:
# Use capital 'X' as multiplication and '^' for power.
# Avoid spaces in formulae Example: for input 'C' the output is 3.14Xradius^2
# Show message 'Enter valid alphabet' for the input other than specified letters
# ------------------------------------------------------------------------------------------------------------
shape = input("Enter shape letter (S/R/T/C): ")
if shape == 'S':
    print("side^2")
elif shape == 'R':
    print("lengthXbreadth")
elif shape == 'T':
    print("0.5XbaseXheight")
elif shape == 'C':
    print("3.14Xradius^2")
else:
    print("Enter valid alphabet")

# ---------------------------------------------------------------------------------------------------------------
# 2. if – else:
# 3 friends are planning a holiday trip. They are searching for their destination. They visited an
# awesome website which helps people to decide the holiday destination in India according to the
# months of the year.
# From February to May -Shimla Manali Ooty
# From June to September - Lonavala Goa Kodaikanal
# From October to January - Munnar Kullu Manali

# Input ----- A single number for the respective month
# Output ----- Suggestion as per the list given
# Example Input ----2
# Output ----- Shimla Manali Ooty
# Note: if number entered is more than 12 then print message "Enter valid number"
# ------------------------------------------------------------------------------------------------------------

month = int(input("Enter month number: "))
if 2 <= month <= 5:
    print("Shimla Manali Ooty")
elif 6 <= month <= 9:
    print("Lonavala Goa Kodaikanal")
elif 10 <= month <= 12 or month == 1:
    print("Munnar Kullu Manali")
else:
    print("Enter valid number")

# ------------------------------------------------------------------------------------------------------------
# 3. if – else:
# Siddesh is an accountant at XYZ company. He is responsible for calculating the income tax of the
# employees in the company. He has the following reference tax slabs according to the new tax regime.
# --------------------------------------------------------------------------
# Income Tax Slab        Tax Rates As Per New Regime
# -------------------------------------------------------------------------
# 0-₹2,50,000            Nil
# ₹2,50,001-₹5,00,000    5%
# ₹5,00,001-₹7,50,000    12500+10% of total income exceeding ₹5,00,000
# ₹7,50,001 - 10,00,000  ₹37500 + 15% of total income exceeding ₹7,50,000
# ₹10,00,001-₹12,50,000  ₹75000 + 20% of total income exceeding ₹10,00,000
# ₹12,50,001-15,00,000   ₹125000 + 25% of total income exceeding ₹12,50,000
# Above ₹ 15,00,000      ₹187500+30% of total income exceeding ₹15,00,000
# ------------------------------------------------------------------------------
# Mohan has given income as the input. Write a python logic to calculate how much income tax is
# deducted annually from his salary.
# Input ----Annual salary in int
# Output ----Total tax
# Example Input ----600000
# Output -----22500
# --------------------------------------------------------------------------------------------------------

income = int(input("Enter annual income: "))
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 750000:
    tax = 12500 + (income - 500000) * 0.10
elif income <= 1000000:
    tax = 37500 + (income - 750000) * 0.15
elif income <= 1250000:
    tax = 75000 + (income - 1000000) * 0.20
elif income <= 1500000:
    tax = 125000 + (income - 1250000) * 0.25
else:
    tax = 187500 + (income - 1500000) * 0.30
print(int(tax))

# ---------------------------------------------------------------------------------------------------------------
# 4. Loops:
# Arvind wants to print leap years starting between the years 2000 and 2100. Write a python logic
# to help him.

# Input
# The first line of input contains the start year The second line of input contains end year

# Note: Both years should be included in answer if they are leap years

# Output -----All leap years

# Example Input
# 2004
# 2030

# Output
# 2004
# 2008
# 2012
# 2016
# 2020
# 2024
# 2028
# -----------------------------------------------------------------------------------------------------------------

start = int(input("Enter start year: "))
end = int(input("Enter end year: "))

for year in range(start, end + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)

# ------------------------------------------------------------------------------------------------------------------
# 5. Loops:
# Ishan is an accountant in a small-scale firm. His job is to make simple calculations using + - * /
# operators frequently. Create a python program to create continuous calculations until he selects Stop.

# Input
# The first input is the first letter of arithmetic operation i.e. "A" for addition, "S" for subtraction,
# "D" for division and "M" for multiplication. second and third line of input is two numbers fourth
# line of input is "Stop"
# Output
# Answers after arithmetic calculations.

# Example Input
# A
# 5
# 3
# Stop
# Output ------8
# --------------------------------------------------------------------------------------------------------------------

while True:
    op = input("Enter operation (A/S/M/D) or Stop: ")
    if op == "Stop":
        break
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if op == "A":
        print(a + b)
    elif op == "S":
        print(a - b)
    elif op == "M":
        print(a * b)
    elif op == "D":
        print(a / b)
    else:
        print("Invalid operation")

# --------------------------------------------------------------------------------------------------------------------
# 6. for loop:
# For a given input integer n and symbol create the following pattern.

# Input
# the first line of the input is the number
# the second line of the input is a symbol
# Output
# Pattern of symbols

# Example Input 1
# 8
# *
# Output 1
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *

# Input 2
# 5
# $
# Output
# $
# $$
# $$$
# $$$$
# $$$$$
# $$$$
# $$$
# $$
# $
# -----------------------------------------------------------------------------------------------------------------

n = int(input("Enter number: "))
symbol = input("Enter symbol: ")

for i in range(1, n + 1):
    print(symbol * i)

# ------------------------------------------------------------------------------------------------------------------
# 7. You are given a string in the input. Print each character of the string in the same line except any
# special character or symbol from "~`!@#$%^&*()<>?//|}{:.".

# Input ---------------String with special characters
# Output --------------string without special characters.
# Example Input ------------abc.xyz#123
# Output -------------abcxyz123
# -------------------------------------------------------------------------------------------------------------------

s = input("Enter string: ")
specials = "~`!@#$%^&*()<>?//|}{ :. "
for ch in s:
    if ch not in specials:
        print(ch, end='')

# ----------------------------------------------------------------------------------------------------------------
# 8. Print the following pattern for different symbols given in input.

# Input
# the first line contains the integer
# second line of the input contains the symbol
# Output
# Print the above given pattern

# Example Input
# 5
# #
# Output
#     #
#    # #
#   # # #
#  # # # #
# --------------------------------------------------------------------------------------------------------------

n = int(input("Enter number: "))
symbol = input("Enter symbol: ")

for i in range(1, n + 1):
    print((symbol + ' ') * i)


#                           ----------------X---------------------
