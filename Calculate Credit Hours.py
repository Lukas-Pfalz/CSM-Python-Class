# Initial Prompt
print("Calculate How Many Credit Hours are required to reach a certain GPA")
print("Make sure you enter decimal-numbers as ##.0")

# credits previously completed
current_credit_hours = float(input("Current Credit-Hours: "))

# current GPA with earned with current credit hours
current_GPA = float(input("Current GPA: "))

# The GPA you are trying to reach
goal_GPA = float(input("GPA Goal: "))

# Calculation for determining the "number of credit hours"
num_hours = current_credit_hours * (goal_GPA - current_GPA) / (4.0 - goal_GPA)

# The required number of credit hours to achieve the goal_GPA is displayed
print("To achieve a GPA of ", goal_GPA, " must earn a 4.0 for ", num_hours, " Credit-Hours")
