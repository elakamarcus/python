#!/bin/python3
"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

"""
p >= 1000
p = a + b + c
c^2 = a^2 + b^2 = (a+b)(a-b)

Source:
https://en.wikipedia.org/wiki/Pythagorean_triple

"""

# import counter to make sorting and counting uniques way too easy
from collections import Counter
# import gcd instead of making my own.. duh...
from math import gcd

def main():
    c = Counter()
    for i in range(2, 1000):
        for j in range(1+ (i % 2), i, 2): #i and j cannot both be odd
            if gcd(i,j)==1: #i and j are coprimes
                perimeter = 2*i*(i+j) #sum up the perimeter, algebra for the win
                if perimeter >= 1001: # can equal too, but not larger than 1000
                    break
                c.update(range(perimeter, 1001, perimeter))
    
    print(c.most_common(1))


if __name__ == '__main__':
    main()

