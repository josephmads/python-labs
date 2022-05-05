# Read up on `range()` and additional options for `print()`.
# Then use a loop to print the following table to the console:
#
# 0 1 2 3 4 5 6 7 8 9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

for num in range(0,50):
    print(num, end = " ")
    if num % 10 == 9:
        print(end = "\n")

# for number in range(0,50):
#     if number == 10:
#         print("\n")
#     elif number == 20:
#         print("\n")
#     elif number == 30:
#         print("\n")
#     elif number == 40:
#         print("\n")
#     else:
#         print(number, end=" ")
    
# for second_line in range(10,20):
#     if number == second_line:
#         print(number, end=" ")
# for third_line in range(20,30):
#     if number == third_line:
#         print(number, end=" ")
# for fourth_line in range(30,40):
#     if number == fourth_line:
#         print(number, end=" ")
# for fifth_line in range(40,50):
#     if number == fifth_line:
#         print(number, end=" ")