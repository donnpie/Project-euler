# Project Euler problem #9
# 2021/11/03
# https://projecteuler.net/problem=9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2+b^2=c^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Elegant solution from https://projecteuler.net/thread=9
# Without programming:

# a= 2mn; b= m^2 -n^2; c= m^2 + n^2;
# a + b + c = 1000;

# 2mn + (m^2 -n^2) + (m^2 + n^2) = 1000;
# 2mn + 2m^2 = 1000;
# 2m(m+n) = 1000;
# m(m+n) = 500;

# m>n;

# m= 20; n= 5;

# a= 200; b= 375; c= 425;

def calc_result_2(a, b, c):
    return a + b + c

def check_squares_2(a, b, c):
    return (a**2 + b**2 - c**2)

# Brute force approach:
for a in range(200, 1000):
    for b in range(a+1, 376):
        for c in range(b+1, 426):
            result = calc_result_2(a, b, c)
            if result == 1000:
                sum_of_squares = check_squares_2(a, b, c)
                if sum_of_squares == 0:
                    print(a, b, c, result, sum_of_squares, a*b*c)
                    break
