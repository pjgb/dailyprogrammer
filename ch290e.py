#!/usr/bin/env python3

# In mathematics, a Kaprekar number for a given base is a non-negative integer,
# the representation of whose square in that base can be split into two parts
# that add up to the original number again. For instance, 45 is a Kaprekar
# number, because 452 = 2025 and 20+25 = 45. 
#
# Your program will receive two integers per line telling you the start and 
# end of the range to scan, inclusively. Example:
#
#     1 50
#
# Your program should emit the Kaprekar numbers in that range. From our example:
#
#     45
#
# Challenge Input:
#
#     2 100
#     101 9000
#
# Challenge Output
#
#     9 45 55 99
#     297 703 999 2223 2728 4879 5050 5292 7272 7777
#


challenges = """2 100
101 9000"""

for line in challenges.split('\n'):
    out = []
    start, end = map(int, line.split(' '))
    for n in range(start, end):
        squared = n**2
        s = str(squared)
        n1 = []
        n2 = []
        for i in range(1, len(s)):
            if int(s[0:i]) + int(s[i:]) == n:
                out.append(n)
    print(out)