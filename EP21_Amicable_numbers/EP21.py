# Project Euler problem #19
# 2021/11/26
# https://projecteuler.net/problem=19

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

# Answer: The sum of amicable numbers is 31626

import math
import time

def get_divisors(num):
    """Returns the divisors of num in a list"""
    divisors = []
    limit = math.floor(math.sqrt(num))
    for i in range(1, limit + 1):
        if num%i == 0:
            divisors.append(i)
            if i != num//i and i != 1:
                divisors.append(num//i)
    return divisors

def add_list(list):
    result = 0
    for num in list:
        result += num
    return result

def find_amicable_nums(upper_limit, tracking_list):
    """Go through numbers in list and check for amicalble numbers"""
    amicable_nums = []
    for i in range(2, upper_limit):
        #print("i:", i)

        # If number is already checked, skip it
        if tracking_list[i] == True:
            #print("{} is already found. Skipping it.".format(i))
            continue

        # Check the first number d(a) = b
        divisors_1 = get_divisors(i)
        total_1 = add_list(divisors_1)
        if total_1 == 1: # Skip the prime numbers
            continue
        tracking_list[i] = True
        if total_1 < upper_limit:
            if tracking_list[total_1] != True:
                tracking_list[total_1] = True
                #print("Marking {} as found".format(total_1))
        else:
            #print("The number {} is out of range".format(total_1))
            continue

        # Check the second number d(b) = a
        divisors_2 = get_divisors(total_1)
        total_2 = add_list(divisors_2)
        #print("{} maps to {}, {} maps to {}]".format(i, total_1, total_1, total_2))

        # Check if number are amicable
        if total_2 == i and i != total_1:
            #print("Found a pair of amicable numbers: [{}, {}]".format(i, total_1))
            amicable_nums.append([i, total_1])

    return amicable_nums

# Driver code

t1 = time.time()

# Declare list to keep track of which numbers have been checked already
upper_limit = 10000
tracking_list = [False for x in range(upper_limit)]
tracking_list[1] = True

amicable_nums = find_amicable_nums(upper_limit, tracking_list)

# Add amicable numbers together
total = 0
for pair in amicable_nums:
    total += pair[0] + pair[1]

print("Amicable numbers:", amicable_nums)
print("The sum of amicable numbers is {}".format(total))

t2 = time.time()
print("Program ran in {} sec".format(t2 - t1))




























