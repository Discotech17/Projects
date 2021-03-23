# Matt Descoteaux
# ENTD200 D003 Winter 2021
# Ms. Cichocki
# Week 4
# 23 Mar 2021

# Problem 1: Calculate gross pay with hours worked * pay rate and return pay.
# Input hours worked
hoursWorked = (input('Enter hours worked: '))

# Pay rate per hour
payRate = (input('Enter pay rate: $'))

# Calculate Pay (missed the int portion) if I wanted to use non-whole numbers I could use float.
grossPay = int(hoursWorked) * int(payRate)

# Tried without anything, didn't return anything.  Tried return inside grossPay and outside.
# Figured I had to print the method of grossPay
print(grossPay)


# Problem 2: Calculate average miles per gallon on trip and return MPG.
# Input car name
carName = (input('Enter your cars name: '))

# Input gas used
gasUsed = (input('Enter the amount of gas used in gallons: '))

# Input the number of miles driven
milesDriven = (input('Enter the number of miles driven: '))

# Calculate MPG. Int used for whole numbers, float for non-whole numbers.
milesPerGallon = int(milesDriven) / int(gasUsed)

# Return Miles Per Gallon
print('Car =', carName,', Gas =', gasUsed,', Miles =', milesDriven,', MPG =', milesPerGallon)
