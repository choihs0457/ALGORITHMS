import sys
from itertools import combinations

N = input()
ans_list = set()

for i in range(len(N)):
    for j in range(i,len(N)):
        ans_list.add(N[i:j+1])

print(len(ans_list))