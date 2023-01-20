import sys

input = sys.stdin.readline

divisor_cnt = input()
divisor = list(map(int, input().split()))

print(max(divisor)*min(divisor))