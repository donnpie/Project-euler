# Project Euler problem #13
# 2021/11/16
# https://projecteuler.net/problem=16

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers...

# What do I need to learn to solve this problem?
# - How to read in a file containing numbers
# - How to add large numbers

x1 = 37107287533902102798797998220837590246510135740250
x2 = 46376937677490009712648124896970078050417018260538

# Step 1: Read the numbers from a file
with open('numbers.txt', 'r') as f:
    lines = f.readlines()
    f.close()

number_of_lines = len(lines)
#print(number_of_lines)

# Get rid of the newline character
for i in range(number_of_lines):
    new_line = lines[i].strip()
    lines[i] = new_line
#print(lines)

# convert strings to numbers
for i in range(number_of_lines):
    new_line = lines[i]
    new_number = int(new_line)
    lines[i] = new_number

#print(lines)

# Add numbers
total = 0
for i in range(number_of_lines):
    total += lines[i]

print(total)





# Resources
# https://www.pythontutorial.net/python-basics/python-read-text-file/
# https://www.geeksforgeeks.org/different-ways-to-clear-a-list-in-python/
