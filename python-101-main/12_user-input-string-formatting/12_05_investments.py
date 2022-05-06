# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

investment = float(input("How much did you invest?: "))
interest = float(input("What is your interest rate?: "))
years = float(input("How many years will you invest?: "))

interest /= 100
roi = ((investment * interest) * years)

print("The value of your investment will be: ", roi + investment)