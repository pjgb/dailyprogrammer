#!/usr/bin/env python3

inputs = [
    ['floor', 'brake'],
    ['wood', 'book'],
    ['a fall to the floor', 'braking the door in'],
]

# Change the a sentence to another sentence, letter by letter.
# The sentences will always have the same length.
# Output the lines where you change one letter and one letter only

for w1, w2 in inputs:
    print(w1)
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            print(w2[0:i+1] + w1[i+1:])
