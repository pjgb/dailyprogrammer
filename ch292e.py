#!/usr/bin/env python3

# We are given a list of numbers in a 'short-hand' range notation where only
# the significant part of the next number is written because we know the
# numbers are always increasing 
#     ex. '1,3,7,2,4,1' represents [1, 3, 7, 12, 14, 21]). 
# 
# Some people use different separators for their ranges
#     ex. '1-3,1-2', '1:3,1:2', '1..3,1..2' 
#     represent the same numbers [1, 2, 3, 11, 12]) 
#     and they sometimes specify a third digit for the range step
#     ex. '1:5:2' represents [1, 3, 5]
#     
# NOTE: For this challenge range limits are always inclusive.
# Our job is to return a list of the complete numbers.
# The possible separators are: ['-', ':', '..']
#
# You'll be given strings in the 'short-hand' range notation
#
#     '1,3,7,2,4,1'
#     '1-3,1-2'
#     '1:5:2'
#     '104-2'
#     '104..02'
#     '545,64:11'
#
# You should output a string of all the numbers separated by a space
#
#     '1 3 7 12 14 21'
#     '1 2 3 11 12'
#     '1 3 5'
#     '104 105 106 107 108 109 110 111 112'
#     '104 105 106...200 201 202'         # truncated for simplicity
#     '545 564 565 566...609 610 611'     # truncated for simplicity

separators = ['-', ':', '..']

inputs = [
    '1,3,7,2,4,1',
    '1-3,1-2',
    '1:5:2',
    '104-2',
    '104..02',
    '545,64:11',
]

for line in inputs:
    line_output = []
    line_ranges = line.split(',')
    for i, r in enumerate(line_ranges):
        range_output = []
        try:
            range_output = [int(r)]
        except ValueError:
            range_numbers = []
            for s in separators:
                if r.count(s):
                    range_numbers = r.split(s)
                    break
            for n in enumerate(range_numbers):
                if len(range_numbers) == 3:
                    if i > 0:
                        
            
        for s in separators:
            if r.count(s):
                sep_found = True
        if not sep_found:
            numbers = int(r)
            if not numbers:
                if r.count(s):
                    numbers = range(*[int(n) for n in r.split(s)])
                
        output.append(numbers)

print(output)