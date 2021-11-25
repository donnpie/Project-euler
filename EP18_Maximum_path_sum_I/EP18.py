# Project Euler problem #18
# 2021/11/25
# https://projecteuler.net/problem=18

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
# it cannot be solved by brute force, and requires a clever method! ;o)

#import math

# Read the numbers from a file - See resource 1
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
