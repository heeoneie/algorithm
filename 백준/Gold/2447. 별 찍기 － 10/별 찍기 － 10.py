import sys
sys.setrecursionlimit(10**6)

def drawStar(n):
    if n == 1:
        return ['*']

    stars = drawStar(n//3) 
    line = []  
   
    for star in stars:
        line.append(star*3)
    for star in stars:
        line.append(star+' '*(n//3)+star)
    for star in stars:
        line.append(star*3)
    return line

n = int(sys.stdin.readline().strip())
print('\n'.join(drawStar(n)))