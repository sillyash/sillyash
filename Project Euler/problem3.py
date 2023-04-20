from math import sqrt

def prime_factor_max(n:int)->int:
    assert n >= 1
    for i in range(1,n):
        if n%i == 0 and is_prime(i):
            x = i
    return x

def is_prime(n:int)->bool:
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

print(prime_factor_max(600851475143))
