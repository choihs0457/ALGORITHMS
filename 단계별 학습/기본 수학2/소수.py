import sys

input = sys.stdin.readline

start_num = int(input())
end_num = int(input())+1

prime_num = []
for num in range(start_num, end_num) :
    fail = 0
    if num > 1 :
        for divisor in range(2, num) :
            if num % divisor == 0:
                fail += 1
                break
        if fail == 0:
            prime_num.append(num)
            
if prime_num :
    print(sum(prime_num))
    print(prime_num[0])
else:
    print(-1)