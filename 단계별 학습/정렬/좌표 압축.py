import sys

input = sys.stdin.readline

N = int(input())
nature_list = []

nature_list = list(map(int, input().split()))
ans_list = sorted(list(set(nature_list)))

dic = {ans_list[i] : i for i in range(len(ans_list))}

for i in nature_list:
    print(dic[i], end = " ")