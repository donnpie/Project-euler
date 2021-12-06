# Project Euler problem #22
# 2021/12/05
# https://projecteuler.net/problem=22

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?

def read_file(file):
    """Read the numbers from a file"""
    with open(file, 'r') as f:
        names = f.read()
        f.close()
    return names

def clean_names(names):
    """Get names into list and remove unnecesary characters"""
    names = names.replace('"', '')
    names = names.split(",")
    return names

def a_value(string):
    """Returns the numerical value of a string"""
    value = 0
    for char in string:
        ascii_val = ord(char) - 64
        value += ascii_val
    return value

# Driver code
names = read_file('names.txt')
names = clean_names(names)
names.sort()
total = 0
for i in range(len(names)):
    value = a_value(names[i])
    position = i + 1
    score = value * position
    total += score

print("The total score is", total)

# Resources
# 01 https://careerkarma.com/blog/python-remove-character-from-string/
# 02 https://www.programiz.com/python-programming/examples/ascii-character
