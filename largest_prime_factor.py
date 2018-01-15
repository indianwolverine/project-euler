import math

def isprime(n):
    limit = math.sqrt(n) // 1
    limit = int(limit)
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True

def largest_prime_factor(n):
    for i in range(2, n + 1):
        factor = n/i
        if (n % i == 0 and isprime(factor)):
            return factor
    return -1
