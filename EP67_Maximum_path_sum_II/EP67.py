# Project Euler problem #67
# 2021/11/25
# https://projecteuler.net/problem=67

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18.
# It is not possible to try every route to solve this problem, as there are 2^99 altogether!
# If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all.
# There is an efficient algorithm to solve it. ;o)

# Read the numbers from a file - See resource 1
with open('p067_triangle.txt', 'r') as f:
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
numbers = []
for i in range(number_of_lines):
    new_line = lines[i].split()
    for n in range(len(new_line)):
        new_number = int(new_line[n])
        new_line[n] = new_number
    numbers.append(new_line)
#print(numbers)

# Get number of rows in numbers array
rows = len(numbers)
#print(rows)

# Use dynamic programming
# Initialise the first column of running totals (column 0)
total =[]
for r in range(0, rows):
    #print("row", r)
    total.append([])
    if r == 0:
        total[r].append(numbers[r][0])
        continue
    #print('numbers[r - 1][0]', numbers[r - 1][0])
    #print('numbers[r][0]', numbers[r][0])
    total[r].append(total[r - 1][0] + numbers[r][0])
#print(total)

# Go through the remainder of columns and calc the max possible value at each node
cols = len(numbers[rows-1])
#print(cols)
for c in range(1, cols):
    for r in range(c, rows):
        if r == c:
            max_val = total[r - 1][c - 1] + numbers[r][c]
            total[r].append(max_val)
            continue
        #print("row", r)
        #print("col", c)
        max_val = max(total[r - 1][c - 1] + numbers[r][c], total[r - 1][c] + numbers[r][c])
        total[r].append(max_val)

#print(total)

max_overall = max(total[rows-1]) # The max path sum can be found as the max value in the last row
print(max_overall)












# Resources
# 01 EP13.py
# 02 https://www.w3schools.com/python/ref_string_split.asp
