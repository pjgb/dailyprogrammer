#!/usr/bin/env python3

# Oh, how cursed we are to have but 10 digits upon our fingers. Imagine the
# possibilities were we able to count to numbers beyond! But halt! 
# With 10 digits upon our two appendages, 1024 unique combinations appear! 
# But alas, counting in this manner is cumbersome, and counting to such a 
# number beyond reason. Surely being able to count up to 100 would suffice!
# 
# You will be given inputs which correspond to the 10 digits of a pair of 
# hands in the following format, where 1 means the finger is raised, 
# and 0 means the finger is down.
#
# Example:
#
#     LP LR LM LI LT RT RI RM RR RP
#     0  1  1  1  0  1  1  1  0  0
#
# L = Left, R = Right
# P = Pinky, R = Ring Finger, M = Middle Finger, I = Index Finger, T = Thumb
# 
# Your challenge is to take these inputs, and:
# Determine if it is valid based on this counting scheme:
#     http://www.wikihow.com/Count-to-99-on-Your-Fingers
# If it is, then decode the inputs into the number represented by the digits on the hand.
#
# Formal Inputs and Outputs
# 
#     0111011100 -> 37
#     1010010000 -> Invalid
#     0011101110 -> 73
#     0000110000 -> 55
#     1111110001 -> Invalid

def fingercounting(s):
    lt = int(s[4])
    rt = int(s[5])
    lf = [int(f) for f in s[0:4]]
    rf = [int(f) for f in s[6:]]
    if not lf[0] <= lf[1] <= lf[2] <= lf[3]:
        return 'Invalid'
    if not rf[0] >= rf[1] >= rf[2] >= rf[3]:
        return 'Invalid'
    s = sum(rf) + rt * 5 + sum(lf) * 10 + lt * 50
    return s


print('Challenge:')
inputs = ['0111011100', '1010010000', '0011101110', '0000110000', '1111110001']
for s in inputs:
    print('{0} -> {1}'.format(s, fingercounting(s)))