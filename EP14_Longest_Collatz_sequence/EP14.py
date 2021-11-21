# Project Euler problem #14
# 2021/11/18
# https://projecteuler.net/problem=14

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# Funtion to generate Collatz sequence (not necessary for solution but interesting)
def collatz(start_num):
    # Returns the sequence itself
    result_array = [start_num]
    current_num = start_num
    result = 2
    counter = 1
    while current_num > 1:
        if current_num % 2 == 0:
            result = current_num // 2
            # print("number is even: ", current_num)
            # print("result: ", result)
        else:
            result = 3 * current_num + 1
            # print("   number is odd: ", current_num)
            # print("   result: ", result)
        result_array.append(result)
        current_num = result
        counter += 1
        #print(counter)
    return result_array

count_the_rest = {1: 1} # Dict holding a count of sequences already counted

def collatz_count(start_num):
    # Returns only the count of terms in the sequence

    #print("starting with ", start_num)

    # Check if the rest of the sequence is already found
    if start_num in count_the_rest:
        #print("start_num found in dictionary")
        return count_the_rest[start_num]

    current_num = start_num
    result = 0
    counter = 1
    while current_num > 1:
        if current_num % 2 == 0:
            result = current_num // 2
            # print("number is even: ", current_num)
            # print("result: ", result)
        else:
            result = 3 * current_num + 1
            # print("   number is odd: ", current_num)
            # print("   result: ", result)
        current_num = result

        #print("counter:", counter)
        if result in count_the_rest:
            #print("result found in dictionary (", result, ")")
            counter += count_the_rest[result]
            break
        counter += 1

    #print("adding result to dictionary")
    count_the_rest[start_num] = counter
    return counter

# Test code
#for i in range(1, 10):
#    print("i: ", i, "count: ", collatz_count(i), "sequence:", collatz(i))
# i = 3
# print("i: ", i, "count: ", collatz_count(i), "sequence:", collatz(i))

# Generate the dictionary with length of all sequences
for i in range(1, 1000000):
    collatz_count(i)

#print(count_the_rest)

max_length = max(count_the_rest.values())
print("max_length:", max_length)
print("starting value with max length:", max(count_the_rest, key=count_the_rest.get)) # See Resource 01

# Resources
# 01. https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
