#!/usr/bin/python3
import scrabble

# look for longest palindrome

longest = ""

for word in scrabble.wordlist:
    is_palindrome = True
    for index in range(len(word)):
        if word[index] != word[-(index+1)]:
            is_palindrome = False
    if is_palindrome and len(word) > len(longest):
        longest = word

print(longest)

longest = ""
# faster version
for word in scrabble.wordlist:
    if word == word[::-1] and len(word) > len(longest):
        longest = word
print(longest)