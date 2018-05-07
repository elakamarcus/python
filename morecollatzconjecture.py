# collatz
# https://en.wikipedia.org/wiki/Collatz_conjecture
#!/usr/bin/python

# Below code to index the number of steps/iterations before n becomes 1.

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
    return len(seq)-1

# testing
for a in range(2, 500, 1):
    if(collatz(a) > 100):
        print"{}, {}".format(a, collatz(a))

iteration='''
for a in range(2, 10, 1):
    print"{} ends with {} steps.".format(a, collatz(a))
'''
poweroftwo='''
a = 2
print"Starting no., iterations."
while a < 1048577:
    print"{}, {}".format(a, collatz(a))
    a *= 2
'''

blob='''
Original code
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
    print"Collatz results:\n Starting at {}\n {} steps until 1.".format(a, len(seq)-1)

collatz(a)
'''
