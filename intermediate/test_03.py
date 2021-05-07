#!/usr/bin/python3
import scrabble

# look for a character that is never repeated

def has_all_vovels(word):
    vovels = "aeiuo"
    for vowel in vovels:
        if vowel not in word:
            return False
    return True

for word in scrabble.wordlist:
    if has_all_vovels(word):
        print(word)