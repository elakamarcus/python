def isPalindrome(n):
    return str(n) == str(n[::-1])

def isMaybePrime(n):
    return n
    #tbc

def isPrime(n):
    return n
    #tbc


def isPandigital(n):
    count = 10*[0]
    while n != 0:
        if count[n%10] == 1: return False
        count[n%10] += 1
        n /= 10
    return True

def collatz(n):
    a=n
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
