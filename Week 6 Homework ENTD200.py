# Matt Descoteaux
# ENTD200 D003 Winter 2021
# Ms. Cichocki
# Week 6
# 07 Apr 2021

# Problem 1: Calculate gross pay with hours worked * pay rate and return pay.
# Input hours worked
#hoursWorked = (input('Enter hours worked: '))

# Pay rate per hour
#payRate = (input('Enter pay rate: $'))

# Calculate Pay (missed the int portion) if I wanted to use non-whole numbers I could use float.
#grossPay = int(hoursWorked) * int(payRate)

# Tried without anything, didn't return anything.  Tried return inside grossPay and outside.
# Figured I had to print the method of grossPay
#print(grossPay)

# This is the new code for gross pay.
# I couldn't start at hoursWorked since I broke it up so simply.
user = input("Enter Employee Name or 'Quit' to Quit: ")
end = "Quit"
while user!=end:
    Hours = int(input("Please enter hours worked: "))
    Rate = int(input("Please enter hourly pay rate: $"))
    if Hours:
        GrossPay = (Rate*Hours)
        print("Employee Name:", user)
        print("Gross Pay: $", GrossPay)
    user = input("If you'd like to continue, type in next employee's name, if not press 'Quit' to exit.")
        
else:
    print("Exiting program....")


# Problem 2: Calculate average miles per gallon on trip and return MPG.
# Input car name
#carName = (input('Enter your cars name: '))

# Input gas used
#gasUsed = (input('Enter the amount of gas used in gallons: '))

# Input the number of miles driven
#milesDriven = (input('Enter the number of miles driven: '))

# Calculate MPG. Int used for whole numbers, float for non-whole numbers.
#milesPerGallon = int(milesDriven) / int(gasUsed)

# Return Miles Per Gallon
#print('Car =', carName,', Gas =', gasUsed,', Miles =', milesDriven,', MPG =', milesPerGallon)

# Same witht his calculation.  I had simplified it too far.
# I used the same code with different inputs as the payroll calculator
vehiclesList = ['Toyota', 'Honda', 'Chevy', 'Ford', 'Mazda', 'Nissan', 'Dodge']
print(vehiclesList)
user = input("Enter your vehicles model or 'Quit' to Quit: ")
end = "Quit"
while user!=end:
    Miles = int(input("Please enter miles driven: "))
    Gas = int(input("Please enter gas used:"))
    if Miles:
        MilesPerGallon = (Miles/Gas)
        print("Model:", user)
        print("Gas Used:", Gas)
        print("Miles driven:", Miles)
        print("MPG:", MilesPerGallon)
    user = input("If you'd like to calculate another vehicle or trip, type in model.  If not type 'Quit' to exit")
        
else:
    print("Exiting program....")