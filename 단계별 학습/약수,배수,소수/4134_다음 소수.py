import sys

input = sys.stdin.readline

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i*i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

cases = int(input())

for _ in range(cases):
    Num = int(input())
    if Num % 2 == 0:
        Num += 1
        while not isPrime(Num):
            Num += 2
        print(Num)
    else:
        while not isPrime(Num):
            Num += 2
        print(Num)