import sys

input = sys.stdin.readline

# 첫 코드 느리지만 정답은 나옴 ㅠ
# while True :
#     start_num = int(input())
#     if start_num == 0 :
#         break
#     prime_num = []
#     end_num = (start_num * 2) + 1
#     start_num += 1
#     for num in range(start_num, end_num) :
#         fail = 0
#         if num > 1 :
#             for divisor in range(2, num) :
#                 if num % divisor == 0:
#                     fail += 1
#                     break
#             if fail == 0:
#                 prime_num.append(num)
#     print(len(prime_num))
# 정답 코드         
limit = 123456

eratos = [1] * (limit * 2 + 1)
eratos[0] = 0
eratos[1] = 0
for i in range(2, int(len(eratos)**0.5)):
    if eratos[i]:
        for j in range(i + i, len(eratos), i):
            eratos[j] = 0
while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(sum(eratos[n+1:(2*n)+1]))