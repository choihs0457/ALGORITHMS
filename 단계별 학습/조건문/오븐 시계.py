H, M = map(int, input().split())
Time = int(input())

if M + Time > 59:
    H = H + (M + Time) // 60
    if H > 23:
        H = H % 24
    M = (M + Time) % 60
else:
    M = M + Time

print(H, end="")
print(" ", end="")
print(M)
