# Project Euler problem #10
# 2021/11/04
# https://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math

#How to find primes?
#A prime is a number that is only divisible by itself and 1
#all primes except 2 are odd numbers
#to test a prime you must divide it by all numbers up to half of the prime
#you dont need divide it by even numbers because primes are always even
#make a list to hold the primes and add the first few primes
#Make a list of numbers
# numbers = [2]
# first_number = 1999901
# last_number = 2000000
# for n in range(first_number,last_number, 2):
#     numbers.append(n)
# #print(numbers)

# primes = []

# for n in numbers:
#     if n == 2 or n == 3 or n == 5:
#         primes.append(n)
#         continue
#     halfway = n//2
#     is_prime = True
#     for denom in range(3, halfway):
#         if n%denom == 0:
#             is_prime = False
#             #print(n, denom, "is not prime")
#             break
#     if is_prime:
#         #print(n, "is prime")
#         primes.append(n)

# print("primes", primes)

# The previous approach is too inefficient to be practical
# Rather implement the "Sieve of Eratosthenes" - see wikipedia article below
n = 2000000

bool_values =  [True for i in range(n)] #Make an array of True values
limit = int(math.sqrt(n))

print(limit)

for i in range(2, limit):
    if bool_values[i]:
        j = i**2
        k = 0
        while j < n:
            bool_values[j] = False
            k += 1
            j = i**2 + k*i

#print(bool_values)

# Make a list of prime numbers
primes = []
for i in range(2, n):
    if (bool_values[i] == True):
        primes.append(i)

#print(primes)

# Add up all the primes
running_total = 0
for i in primes:
    running_total += i

print("sum of primes:", running_total)


# Resoures
# https://www.journaldev.com/33182/python-add-to-list
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# https://www.geeksforgeeks.org/python-boolean-list-initialization/
# https://www.geeksforgeeks.org/python-math-function-sqrt/
