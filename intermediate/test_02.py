#!/usr/bin/python3
import scrabble

import string

# look for a character that is never repeated

for letter in string.ascii_lowercase:
    exists = False
    for word in scrabble.wordlist:
        if letter * 2 in word:
            exists = True
            break
    if not exists:
        print("There are no English words with a double " + letter)