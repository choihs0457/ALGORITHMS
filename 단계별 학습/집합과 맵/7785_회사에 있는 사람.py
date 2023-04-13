import sys

input = sys.stdin.readline

sample = int(input())
result = list()
entered = {}
for _ in range(sample):
    name, state = input().split()
    if state == 'enter':
        entered[name] = state
    else:
        entered.pop(name)
for enter in entered.keys():
    result.append(enter)
print(entered.keys())
# result.sort(reverse=True)
# print("\n".join(result))

# 4
# Baha enter
# Askar enter
# Baha leave
# Artem enter