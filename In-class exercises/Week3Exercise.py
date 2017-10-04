
'''
# Leap year
# A leap year is divisible by 4 and it's not divisible by 100
# Or it's simply divisible by 400
# Finish this short program so that it
# let's the user know if the year is a leap year
year = eval(input("Enter year: "))

# Boolean value
# Hint: Use the mod operator (%) to know if y is divisible by x
isLeapYear = ?

if isLeapYear: # same as if isLeapYear == True:
	print(year, "is a leap year")
else:
	print(year, "is not a leap year")
'''

'''
# Making a subtraction quiz
import random

# 1. Generate two random single-digit integers between 0 and 9
n1 = ?
n2 = ?

# 2. Swap the numbers if number2 is greater than number 1 (no negative answers)
if ?
	# Hint: Use simultaneous assignments to swap the numbers

# 3. Prompt the student to answer "What is number1 - number2?" 12 
answer = eval(input("What is "+ str(n1) + " - " + str(n2) + "? "))

# 4. Check the answer and display the result
if ?
	# print if they're wrong or correct
else:
	# if they're wrong, make sure to say what the correct answer for n1 - n2 is

'''

'''
# Computing BMI

# Prompt the user to enter weight in pounds
weight = eval(input("Enter weight in pounds: "))
# Prompt the user to enter height in inches
height = eval(input("Enter height in inches: "))
KILOGRAMS_PER_POUND = 0.45359237 # Constant
METERS_PER_INCH = 0.0254 # Constant

# Compute BMI
weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = height * METERS_PER_INCH
bmi = weightInKilograms / (heightInMeters * heightInMeters)
# Display result
print("BMI is", format(bmi, ".2f"))

# check if the user is underweight, normal, overweight or obese
# use if-elif-else statements
# bmi under 18.5 is underweight
# bmi between 18.5 and below 25 is normal
# bmi between 25 and below 30 is overweight
# bmi over 30 is obese

if elif else ?

'''