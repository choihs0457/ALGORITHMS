N = int(input())
 
for i in range(2, int(N ** 0.5) + 1):
    while(N > 1):
        if(N % i == 0):
            N //= i
            print(i)
        else:
            break
 
if(N > 1): print(N)