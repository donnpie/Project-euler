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

# The answer is 4179871

import math
import time

def get_abundant_nums(first_num, last_num):
    """Returns a list of abundant numbers for the range between first_num and last_num (inclusive)"""
    abundant_nums = []
    for num in range(first_num, last_num + 1):
        limit = math.floor(math.sqrt(num))
        sum_of_divisors = 0
        for i in range(1, limit + 1): # Find proper divisors of num
            if num%i == 0:
                sum_of_divisors += i
                if i != num//i and i != 1:
                    sum_of_divisors += num//i
        if sum_of_divisors > num:
            abundant_nums.append(num)
    return abundant_nums

def add_list(list): # Copied from EP21
    result = 0
    for num in list:
        result += num
    return result

# Driver code
t1 = time.time()

# Find all abundant numbers < 28123
upper_lim = 28123
abundant_nums = get_abundant_nums(2, upper_lim)

t2 = time.time()
print("Segment 1 ran in {} sec".format(t2 - t1))

# Find all the sums of pairs of abundant nums
sums_set = set(())
for i in range(len(abundant_nums)):
    for j in range(i, len(abundant_nums)):
        the_sum = abundant_nums[i] + abundant_nums[j]
        if the_sum > upper_lim:
            break
        sums_set.add(the_sum)

t3 = time.time()
print("Segment 2 ran in {} sec".format(t3 - t2))

# Find the numbers that cannot be represented as the sum of two abundant numbers
max_sum = max(sums_set)
all_nums = {x for x in range(1, max_sum + 1)}
not_abundant_sums = all_nums - sums_set

answer = add_list(not_abundant_sums) # Turns out this way is faster than using the reduce function
print("The answer is", answer)

t4 = time.time()
print("Segment 3 ran in {} sec".format(t4 - t3))

# Resources
# 01 https://www.geeksforgeeks.org/switch-case-in-python-replacement/
# 02 https://www.tutorialspoint.com/enum-in-python
# 03 https://www.w3schools.com/python/python_sets.asp
# 04 https://www.geeksforgeeks.org/set-add-python/
# 05 https://www.geeksforgeeks.org/python-convert-set-into-a-list/
# 06 https://python-reference.readthedocs.io/en/latest/docs/comprehensions/set_comprehension.html
