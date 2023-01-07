import sys

input = sys.stdin.readline

while True :
    start_num = int(input())
    if start_num == 0 :
        break
    prime_num = []
    end_num = (start_num * 2) + 1
    start_num += 1
    for num in range(start_num, end_num) :
        fail = 0
        if num > 1 :
            for divisor in range(2, num) :
                if num % divisor == 0:
                    fail += 1
                    break
            if fail == 0:
                prime_num.append(num)
    print(len(prime_num))
          
