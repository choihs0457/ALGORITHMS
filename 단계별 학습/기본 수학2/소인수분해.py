import sys

input = sys.stdin.readline

N = int(input())**0.5
divisor = 2
while divisor <= N :
    if N % divisor == 0:
        print(divisor)
        N = N / divisor
    else:
        divisor += 1

# 더 빠른 코드
# N = int(input())
 
# for i in range(2, int(N ** 0.5) + 1):
#     while(N > 1):
#         if(N % i == 0):
#             N //= i
#             print(i)
#         else:
#             break
 
# if(N > 1): print(N)