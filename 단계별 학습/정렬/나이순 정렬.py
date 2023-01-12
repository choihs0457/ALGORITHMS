import sys

input = sys.stdin.readline

# N = int(input().rstrip())
# ans_dict = {}

# for i in range(N) :
#   x, y = map(str, input().rstrip().split())
#   x = int(x)
#   ans_dict[y] = x

# sorted_dict = sorted(ans_dict.items(), key = lambda item: item[1])
# for j in sorted_dict:
#   print(j[1],j[0])
# 왜 안되는지 모르겠음

import sys
n = int(sys.stdin.readline())
member = []
for i in range(n):
    member.append(list(sys.stdin.readline().split()))
member.sort(key=lambda x: int(x[0]))
for i in range(n):
    print(member[i][0], member[i][1])