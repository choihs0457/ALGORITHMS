import sys

input = sys.stdin.readline

S = list(map(str, input().rstrip()))
I = int(input())

print(S[I-1])