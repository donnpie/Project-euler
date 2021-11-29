# Project Euler problem #20
# 2021/11/26
# https://projecteuler.net/problem=20

# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

# Check if an index is within range
def index_is_in_range(list, index):
    # Index must be a non-negative number
    return(index < len(list))

factorials = [0]
def factorial(num):
    if index_is_in_range(factorials, num):
        return factorial[num]
    if num <= 1:
        factorials.append(1)
        return 1
    else:
        fact = num*factorial(num - 1)
        factorials.append(fact)
        return fact

factorial(100)
#print(factorials)

# Convert number to string
number = factorials[-1]
string = str(number)
print(string)

# Add digits together
result = 0
for letter in string:
    num = int(letter)
    result += num
    #print(letter)
print(result)

# Resources
# 01 https://www.kite.com/python/answers/how-to-check-if-an-index-exists-in-a-list-in-python
