# Project Euler problem #23
# 2021/12/06
# https://projecteuler.net/problem=23

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be
# expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# Approach to the problem
# Find all the abundant numbers < 28123 and store in a list
    # For each number find the proper divisors then check for deficienct/perfection/abundance
# Find the sums of all pairs of abundant numbers
# Store these values in a list
# Sort the list from smallest to largest
# Iterate through the range 1 to 28123. If a number is not contain in the list then it is not the sum of two abundant numbers. Add this number to a new list (call it not_abundant_sum)
# Add all these number together

import enum
import math
import time

def get_divisors(num): #Copied from EP21
    """Returns a list of the proper divisors of num"""
    divisors = []
    limit = math.floor(math.sqrt(num))
    for i in range(1, limit + 1):
        if num%i == 0:
            divisors.append(i)
            if i != num//i and i != 1:
                divisors.append(num//i)
    return divisors

def add_list(list): #Copied from EP21
    result = 0
    for num in list:
        result += num
    return result

class NumType(enum.Enum):
    abundant = 1
    deficient = 2
    perfect = 3

def check_abundance(num):
    """Retuns 'abundant' if sum of num's proper divisors > num,
    Retuns 'deficient' if sum of num's proper divisors < num
    Retuns 'perfect' if sum of num's proper divisors = num
    """
    divisors = get_divisors(num)
    total = add_list(divisors)
    result = total - num
    if result > 0:
        return NumType.abundant.name
    elif result < 0:
        return NumType.deficient.name
    else:
        return NumType.perfect.name

# Test code
#print(check_abundance(12))

# Driver code
t1 = time.time() #start time to test how long the program runs

# Find all abundant numbers < 28123
upper_lim = 28123
abundant_nums = []
for x in range(2, upper_lim + 1):
    result = check_abundance(x)
    if result == NumType.abundant.name:
        abundant_nums.append(x)

#print(abundant_nums)
t2 = time.time()
print("Segment 1 ran in {} sec".format(t2 - t1))

# Find all the sums of pairs of abundant nums
# sums = []
# for i in range(len(abundant_nums)):
#     for j in range(i, len(abundant_nums)):
#         #print(i, j)
#         the_sum = abundant_nums[i] + abundant_nums[j]
#         if the_sum > upper_lim:
#             break
#         if the_sum not in sums:
#             sums.append(the_sum)

# sums.sort()
# print(sums)

sums_set = set(())
for i in range(len(abundant_nums)):
    for j in range(i, len(abundant_nums)):
        #print(i, j)
        the_sum = abundant_nums[i] + abundant_nums[j]
        if the_sum > upper_lim:
            break
        sums_set.add(the_sum)

sums=list(sums_set)
sums.sort()
#print(sums)

t3 = time.time()
print("Segment 2 ran in {} sec".format(t3 - t2))

# Find the numbers that cannot be represented as the sum of two abundant numbers
max_sum = max(sums)
print("max_sum", max_sum)

not_abundant_sums = []
for i in range(1, max_sum):
    if i not in sums:
        not_abundant_sums.append(i)

#print(not_abundant_sums)

answer = add_list(not_abundant_sums)
print("The answer is", answer)

t4 = time.time()
print("Segment 3 ran in {} sec".format(t4 - t3))

# Resources
# 01 https://www.geeksforgeeks.org/switch-case-in-python-replacement/
# 02 https://www.tutorialspoint.com/enum-in-python
# 03 https://www.w3schools.com/python/python_sets.asp
# 04 https://www.geeksforgeeks.org/set-add-python/
# 05 https://www.geeksforgeeks.org/python-convert-set-into-a-list/












