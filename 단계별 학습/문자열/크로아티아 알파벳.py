from sys import stdin

input = stdin.readline

a = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
b = input()
for i in a:
    b = b.replace(i, "a")
print(len(b))
