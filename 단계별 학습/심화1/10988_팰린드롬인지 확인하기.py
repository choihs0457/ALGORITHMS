wording = input().rstrip()
for i,value in enumerate(wording):
    if value == wording[-i-1]:
        if i == len(wording)-1:
            print(1)
        continue
    else:
        print(0)
        break