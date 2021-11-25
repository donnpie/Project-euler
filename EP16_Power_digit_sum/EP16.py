# Project Euler problem #16
# 2021/11/21
# https://projecteuler.net/problem=16

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000

#print(2**1000)

x = 2**1000

string = str(x)

print(string)

total  = 0
for char in string:
    num = int(char)
    total += num
print("Sum of digits:", total)



