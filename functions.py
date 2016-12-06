def isPalindrome(n):
    return str(n) == str(n[::-1])

def isMaybePrime(n):
    return n

def isPrime(n):
    return n

def isPandigital(n):
    count = 10*[0]
    while a != 0:
        if count[a%10] == 1: return False
        count[a%10] += 1
        a /= 10
    return True

