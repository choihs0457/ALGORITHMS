import sys

input = sys.stdin.readline

# 시간초과 ㅠ
# start_num, end_num = map(int, input().split())

# prime_num = []
# for num in range(start_num, end_num + 1) :
#     fail = 0
#     if num > 1 :
#         for divisor in range(2, num) :
#             if num % divisor == 0:
#                 fail += 1
#                 break
#         if fail == 0:
#             prime_num.append(num)
            
# for _ in prime_num :
#     print(_)

# 정답 코드         

start_num, end_num = map(int, input().split())

eratos = [True]*(end_num+1)
eratos[0] = False
eratos[1] = False

for i in range(2,int(end_num**0.5)+1):
	if eratos[i]:
		for j in range(i*2,end_num+1,i):
			eratos[j] = False

for i in range(start_num,end_num+1):
	if eratos[i]:
		print(i)