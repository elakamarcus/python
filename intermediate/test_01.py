import scrabble

# import all words containing "uu"

for word in scrabble.wordlist:
    if "uu" in word:
        print(word)