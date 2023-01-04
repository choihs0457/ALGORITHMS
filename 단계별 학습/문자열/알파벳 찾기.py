import sys
from string import ascii_lowercase

input = sys.stdin.readline

ans = list(-1 for _ in range(26))
abc_list = list(ascii_lowercase)
S = input().rstrip()

for i, val in enumerate(S):
    if ans[abc_list.index(val)] == -1:
        ans[abc_list.index(val)] = i
for _ in ans:
    print(_, end=" ")

"""
s = input()
for i in range(97,123):
    print(s.find(chr(i)), end=' ')
"""
