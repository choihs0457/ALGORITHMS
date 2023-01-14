import sys

input = sys.stdin.readline

def star_point(N):
    if N == 1:
        return '*'
    
    stars = star_point(N//3)
    ans = []
    for point in stars:
        ans.append(point * 3)
    for point in stars:
        ans.append(point + ' ' * (N//3) + point)
    for point in stars:
        ans.append(point * 3)
    return ans
    


N = int(input())
print('\n'.join(star_point(N)))
