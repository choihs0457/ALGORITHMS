import sys

input = sys.stdin.readline

T_case = int(input())
# for _ in range(T_case):
#     a, b = map(int, input().split())
#     print(a + b)
while T_case:
    T_case -= 1
    a, b = map(int, input().split())
    print(a + b)
