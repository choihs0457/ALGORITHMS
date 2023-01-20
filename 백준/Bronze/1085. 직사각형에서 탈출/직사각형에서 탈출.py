a, b, c, d = map(int, (input().split()))

if c-a < a:
    e = c-a
else:
    e = a

if d-b < b:
    f = d-b
else:
    f = b

if e > f:
    print(f)
else:
    print(e)

