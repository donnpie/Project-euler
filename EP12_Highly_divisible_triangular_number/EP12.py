# Project Euler problem #12
# 2021/11/12
# https://projecteuler.net/problem=12

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

# Step 1: write a function to recursively list the triangle numbers using memoisation
def idx_exists(idx, array):
    if idx >= 0 and idx < len(array):
        return True
    else:
        return False

triangles = [0] # List of triangular numbers
def calc_triangle_number(idx):
    if idx_exists(idx, triangles):
        return triangles[idx]
    if idx == 1:
        triangles.append(1)
        return triangles[idx]
    else:
        number =  calc_triangle_number(idx - 1) + idx
        triangles.append(number)
        return number

# for idx in range(10000):
#     print(calc_triangle_number(idx))

for i in range(1, 100):
    calc_triangle_number(500*i)
#print(triangles)

# Step 2: write a function that calculates and counts the factors for a given triangle number
# break number into its prime factors
# x = a^m * b^n * c^p
# number of factors = (m+1)(n+1)(p+1)
# Copy of solution by iGbanam; see stackoverflow article below
def count_divisors(number):
    limit = number
    number_of_divisors = 1
    i = 2
    while i < limit:
        #print("i: ", i)
        if number % i == 0:
            #print("number % i is True")
            limit = number / i
            #print("limit: ", limit)
            number_of_divisors += 1
            #print("number_of_divisors: ", number_of_divisors)
        #else:
            #print("number % i is False")
        i += 1
    return number_of_divisors * 2

#print("number_of_divisors:", count_divisors(100))

# Step 3: Loop through the triangle numbers starting at 1 and check the number of factors. Stop when the number of factors exceeds 500
for number in triangles:
    number_of_divisors = count_divisors(number)
    #print("number: ", number, "result: ", number_of_divisors)
    if number_of_divisors > 500:
        break
print("number: ", number, "result: ", number_of_divisors)

# Resources
# https://www2.math.upenn.edu/~deturck/m170/wk2/numdivisors.html#:~:text=In%20general%2C%20if%20you%20have,exponents%20%2B%201%22s%20together.
# https://www.google.com/search?q=fast+way+to+calculate+number+of+divisors&oq=fast+way+to+calculate+number+of+divisors&aqs=chrome..69i57j0i22i30j0i390l3.17330j0j7&sourceid=chrome&ie=UTF-8
# https://stackoverflow.com/questions/110344/algorithm-to-calculate-the-number-of-divisors-of-a-given-number














