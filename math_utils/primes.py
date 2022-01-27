from math import sqrt
def isprime(n):
    m = 0
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
            exit
    return True
