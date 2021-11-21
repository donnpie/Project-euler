# Project Euler problem #17
# 2021/11/21
# https://projecteuler.net/problem=17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

# Approach
# Write a function that generates the words for a corresponding number
# Write another function that calculates the lengths of the words
# Store all the word lengths in a dictionary
# Add the lengths of all the words

# Basic number parts
ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
tens = {10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
hundreds = {100: "onehundred", 200: "twohundred", 300: "threehundred", 400: "fourhundred", 500: "fivehundred", 600: "sixhundred", 700: "sevenhundred", 800: "eighthundred", 900: "ninehundred"}
thousands = {1000: "onethousand"}

# Round number down
def round_down(number):
    # Only works for 100's and 10's
    if number // 100 >= 1:
        return (number // 100)*100
    if number // 10 >= 1:
        return (number // 10)*10
    else:
        return 0

#print(round_down(50))

# Convert number to word
def number_to_words(number):
    words = ""
    # Test for 1000
    if number // 1000 == 1:
        words += thousands[1000]
        number -= 1000
    # Test if number has hundreds
    if number // 100 >= 1:
        hundreds_count = round_down(number)
        words += hundreds[hundreds_count]
        if number % 100 != 0:
            words += "and"
        number -= hundreds_count
    # Test if number has tens
    if number // 10 >= 2:
        tens_count = round_down(number)
        words += tens[tens_count]
        number -= tens_count
    if number // 10 == 1:
        words += teens[number]
        return words
    # test for numbers containing no tens
    if number // 1 <= 9 and number // 1 >= 1:
        words += ones[number]
    return words
#print(number_to_words(908))

# Convert words to letter count
def get_letter_count(word):
    return len(word)

# Generate letter counts for each word
counts ={}
start = 1
end = 1001
for i in range(start, end):
    words = number_to_words(i)
    count = get_letter_count(words)
    counts[i] = count

#print(counts)

# Add all the letter counts together
sum=0
for index in range (start, end):
    sum += counts[index]
print("result:", sum)
