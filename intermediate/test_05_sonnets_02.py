#!/usr/bin/python3
import time
my_words = [elt.strip() for elt in open("sonnet_words.txt","r").readlines()]
word_list = [elt.strip() for elt in open("sowpods.txt","r").readlines()]
word_set = set(word_list)
#word_dict = dict((elt, 1) for elt in word_list)

counter = 0

start = time.time()

for word in my_words:
#    if word not in word_list: # 5 seconds
    if word not in word_set: # 0.0 seconds
        print(word)
        counter += 1

stop = time.time()

print(f'Total new words: {counter}')
print(f'Time elapsed: {stop-start:.1f} seconds')