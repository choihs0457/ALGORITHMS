import sys

input = sys.stdin.readline

N = input()

sample_list = list(map(int, input().split()))
print(min(sample_list), max(sample_list))
