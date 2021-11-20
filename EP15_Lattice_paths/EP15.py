# Project Euler problem #15
# 2021/11/20
# https://projecteuler.net/problem=15

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# Solve using dynamic programming
# For an m rows by n colums array
# There is exactly 1 way to reach array[0, 0]


# Declare an n by m array
# Rows go top to bottom and use index i
# Columns go right to left and use index j
rows, cols = (21, 21)
# arr = [[0]*cols]*rows # Don't use this - see resource 3
arr = [[0 for j in range(cols)] for i in range(rows)]

# Initialise top row and left column to 1s
# There is 1 way to reach a cell in the top row or left column
for i in range(rows):
    arr[i][0] = 1

for j in range(cols):
    arr[0][j] = 1

# Calculate the ways to reach each cell
# The number of ways to reach a cell is the sum of the number of ways to reach the cell to the left and the number of ways to reach the cell to the top of it
for j in range(1, cols):
    for i in range(1, rows):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

print("result:", arr[rows-1][cols-1])





print(arr)



















# Resources
# 01. https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
# 02. https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Traverse%20Graph
# 03. https://stackoverflow.com/questions/9459337/assign-value-to-an-individual-cell-in-a-two-dimensional-python-array
