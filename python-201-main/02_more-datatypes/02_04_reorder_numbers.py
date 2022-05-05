# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1

even_list = []
odd_list = []
u_in = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
final_result = ""

for even in range(10):
    if even % 2 == 0:
        even_list.append(even)

for odd in range(10):
    if odd % 2 != 0:
        odd_list.append(odd)

even_list.reverse()
index_list = odd_list + even_list

for i in index_list:
    final_result += (u_in[i] + ", ")
    
print(final_result)

# below is the first way I solved it.

'''
nums = 0
num_list = []

while nums != 10:
    u_in = int(input("enter a number: "))
    num_list.append(u_in)
    nums = len(num_list)

print(num_list[1], num_list[3], num_list[5], num_list[7], num_list[9], 
num_list[8], num_list[6], num_list[4], num_list[2], num_list[0])
'''