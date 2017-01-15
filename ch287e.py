#!/usr/bin/env python3

# Write a function that, given a 4-digit number, returns the largest digit
# in that number. Numbers between 0 and 999 are counted as 4-digit numbers
# with leading 0's.
#
#     largest_digit(1234) -> 4
#     largest_digit(3253) -> 5
#     largest_digit(9800) -> 9
#     largest_digit(3333) -> 3
#     largest_digit(120) -> 2
#
# In the last example, given an input of 120, we treat it as the 4-digit
# number 0120.
#
# Bonus 1
# Write a function that, given a 4-digit number, performs the "descending 
# digits" operation. This operation returns a number with the same 4 digits
# sorted in descending order.
# 
#     desc_digits(1234) -> 4321
#     desc_digits(3253) -> 5332
#     desc_digits(9800) -> 9800
#     desc_digits(3333) -> 3333
#     desc_digits(120) -> 2100
#
# Bonus 2
# Write a function that counts the number of iterations in Kaprekar's Routine,
# which is as follows.
# Given a 4-digit number that has at least two different digits, take that
# number's descending digits, and subtract that number's ascending digits. 
# For example, given 6589, you should take 9865 - 5689, which is 4176. 
# Repeat this process with 4176 and you'll get 7641 - 1467, which is 6174.
# Once you get to 6174 you'll stay there if you repeat the process. 
# In this case we applied the process 2 times before reaching 6174, 
# so our output for 6589 is 2.
#
#     kaprekar(6589) -> 2
#     kaprekar(5455) -> 5
#     kaprekar(6174) -> 0
#
# Numbers like 3333 would immediately go to 0 under this routine, but since we
# require at least two different digits in the input, all numbers will
# eventually reach 6174, which is known as Kaprekar's Constant.


def largest_digit(n):
    digits = [int(d) for d in str(n).zfill(4)]
    return max(digits)

print(largest_digit(1234))
print(largest_digit(3253))
print(largest_digit(9800))
print(largest_digit(3333))
print(largest_digit(120))

# Bonus 1
def desc_digits(n, reverse=False):
    digits = [int(d) for d in str(n).zfill(4)]
    sorted_digits = sorted(digits, reverse=(not reverse))
    return ''.join([str(i) for i in sorted_digits])

print(desc_digits(1234))
print(desc_digits(3253))
print(desc_digits(9800))
print(desc_digits(3333))
print(desc_digits(120))

# Bonus 2
def kaprekar(n, i=0):
    digits = [int(d) for d in str(n).zfill(4)]
    if len(set(digits)) < 2:
        raise ValueError('number has less than 2 different digits')
    asc = int(desc_digits(n, reverse=True))
    desc = int(desc_digits(n))
    current = desc - asc
    if n == current:
        return i
    else:
        return kaprekar(current, i+1)

print(kaprekar(1234))
print(kaprekar(3253))
print(kaprekar(9800))
print(kaprekar(3333))
print(kaprekar(120))

record = 0
for i in range(1,9998):
    try:
        current = kaprekar(i)
        record = (current if record < current else record)
    except ValueError:
        continue

print(record)    # 7