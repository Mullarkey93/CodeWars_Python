# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, and u as vowels for this Kata.
#
# The input string will only consist of lower case letters and/or spaces.
# import unittest

def getCount(inputStr):
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for c in list(inputStr):
        if c in vowels: num_vowels += 1
    return num_vowels

def getCount2(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")