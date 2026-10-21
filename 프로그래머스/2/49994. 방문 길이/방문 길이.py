def solution(dirs):
    moves = {'U': (0,1), 'D': (0,-1), 'R': (1,0), 'L': (-1,0)}
    x, y = 0, 0
    roads = set()
    
    for d in dirs:
        dx, dy = moves[d]
        nx, ny = x + dx, y + dy
        if nx > 5 or ny > 5 or nx < -5 or ny < -5:
            continue
        roads.add(((x,y), (nx, ny)))
        roads.add(((nx,ny), (x, y)))
        x, y = nx, ny
        
    return len(roads) // 2