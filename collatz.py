# collatz
# https://en.wikipedia.org/wiki/Collatz_conjecture
#!/usr/bin/python

import sys

a = int(sys.argv[1])

def collatz(n):
    seq = [n]
    
    if n < 1:
        return []
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        seq.append(n)
    print"Collatz results:\n Starting at {}\n {} steps until 1.".format(a, len(seq))

collatz(a)
