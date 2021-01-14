# Name: Lukas Pfalz
# Section: CSC-1110-71762
# Date: 7/5/20
# Description: Lowest Number
# Assignment # - 3

##### Template for Assignment X, problems 1-X ######

print("********** Problem 3 **********")

# Prints the initial prompt before program begins
print("Weekly Pay Calculator")

# User inputs employee's hours worked during the week

# Hours that week ( Hrs )
hours_worked = int(input("Enter the employee's hours worked this week: "))
# Hourly Pay ( $ / Hr )
hourly_pay = float(input("Enter the employee's hourly pay: "))

# Calculates total pay (pay = hours worked x hourly pay)
pay = hours_worked * hourly_pay

# Prints our the employee's pay for the week
print("\nThe employee's pay: $", format(pay, '.2f'))
