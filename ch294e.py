#!/usr/bin/env python3

# Today's challenge is inspired by the board game Scrabble. Given a set of 7
# letter tiles and a word, determine whether you can make the given word 
# using the given tiles.
# Examples:
# 
#     scrabble("ladilmy", "daily") -> true
#     scrabble("eerriin", "eerie") -> false
#     scrabble("orrpgma", "program") -> true
#     scrabble("orppgma", "program") -> false
#

from collections import Counter

def scrabble(tiles, word):
    ctiles = Counter(tiles.lower())
    cword = Counter(word.lower())
    for letter in cword:
        if cword[letter] > ctiles[letter]:
            return False
    return True

print('Challenge:')
print(scrabble("ladilmy", "daily"))
print(scrabble("eerriin", "eerie"))
print(scrabble("orrpgma", "program"))
print(scrabble("orppgma", "program"))


# Optional Bonus 1
# 
# Handle blank tiles (represented by "?"). These are "wild card" tiles that 
# can stand in for any single letter.
#
#     scrabble("pizza??", "pizzazz") -> true
#     scrabble("piizza?", "pizzazz") -> false
#     scrabble("a??????", "program") -> true
#     scrabble("b??????", "program") -> false
#

from collections import Counter

def scrabble(tiles, word):
    ctiles = Counter(tiles.lower())
    cword = Counter(word.lower())
    cword.subtract(ctiles)
    wildcards = ctiles['?']
    for letter in cword.elements():
        ctiles['?'] -= 1
        if ctiles['?'] < 0:
            return False
    return True

print('Bonus 1:')
print(scrabble("pizza??", "pizzazz"))
print(scrabble("piizza?", "pizzazz"))
print(scrabble("a??????", "program"))
print(scrabble("b??????", "program"))


# Optional Bonus 2
#
# Given a set of up to 20 letter tiles, determine the longest word from the
# enable1 English word list that can be formed using the tiles.
#
#     longest("dcthoyueorza") ->  "coauthored"
#     longest("uruqrnytrois") -> "turquois"
#     longest("rryqeiaegicgeo??") -> "greengrocery"
#     longest("udosjanyuiuebr??") -> "subordinately"
#     longest("vaakojeaietg????????") -> "ovolactovegetarian"
#
# (For all of these examples, there is a unique longest word from the list.
# In the case of a tie, any word that's tied for the longest is a valid output.)
# 


from collections import Counter

def longest(tiles, wordlist_path='./enable1.txt'):
    num_tiles = len(tiles)
    record = 0
    winner = ''
    with open(wordlist_path, 'r') as f:
        for word in f:
            word = word.rstrip()
            word_length = len(word)
            if word_length > num_tiles:
                continue
            match = scrabble(tiles, word)
            if match and word_length > record:
                record = word_length
                winner = word
    return winner

print('Bonus 2:')
print(longest("dcthoyueorza"))
print(longest("uruqrnytrois"))
print(longest("rryqeiaegicgeo??"))
print(longest("udosjanyuiuebr??"))
print(longest("vaakojeaietg????????"))


# Optional Bonus 3
# 
# Consider the case where every tile you use is worth a certain number of 
# points, given on the Wikpedia page for Scrabble. E.g. a is worth 1 point, 
# b is worth 3 points, etc.
# For the purpose of this problem, if you use a blank tile to form a word, 
# it counts as 0 points. For instance, spelling "program" from "progaaf????" 
# gets you 8 points, because you have to use blanks for the m and one of 
# the rs, spelling prog?a?. This scores 3 + 1 + 1 + 2 + 1 = 8 points, 
# for the p, r, o, g, and a, respectively.
# Given a set of up to 20 tiles, determine the highest-scoring word from the 
# word list that can be formed using the tiles.
# 
#     highest("dcthoyueorza") ->  "zydeco"
#     highest("uruqrnytrois") -> "squinty"
#     highest("rryqeiaegicgeo??") -> "reacquiring"
#     highest("udosjanyuiuebr??") -> "jaybirds"
#     highest("vaakojeaietg????????") -> "straightjacketed"


from collections import Counter

p = [('?', 0)]
p.extend([(a, 1) for a in 'eaionrtlsu'])
p.extend([(a, 2) for a in 'dg'])
p.extend([(a, 3) for a in 'bcmp'])
p.extend([(a, 4) for a in 'fhvwy'])
p.extend([(a, 5) for a in 'k'])
p.extend([(a, 8) for a in 'jx'])
p.extend([(a, 10) for a in 'qz'])

points = dict()
points.update(p)

def score_tiles(tiles, word):
    ctiles = Counter(tiles)
    cword = Counter(word)
    score = 0
    for letter in cword:
        score += cword[letter] * points[letter]
        if ctiles[letter] < cword[letter]:
            score -= abs(ctiles[letter]-cword[letter]) * points[letter]
    return score

def highest(tiles, wordlist_path='./enable1.txt'):
    num_tiles = len(tiles)
    record = 0
    winner = ''
    with open(wordlist_path, 'r') as f:
        for word in f:
            word = word.rstrip()
            match = scrabble(tiles, word)
            if match:
                score = score_tiles(tiles, word)
                if score > record:
                    record = score
                    winner = word
    return winner

print('Bonus 3:')
print(highest("dcthoyueorza"))
print(highest("uruqrnytrois"))
print(highest("rryqeiaegicgeo??"))
print(highest("udosjanyuiuebr??"))
print(highest("vaakojeaietg????????"))





