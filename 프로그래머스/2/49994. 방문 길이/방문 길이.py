def solution(dirs):
    # 명령어가 들어왔을때 좌표 얼마나 움직이는지
    direct = {'U': (0,1), 'D': (0,-1), 'R': (1,0), 'L': (-1,0)}
    # 현재 좌표
    x, y = 0, 0
    # 거리 입력 받고 움직인 좌표 저장
    roads = set()
    for d in dirs:
        dx, dy = direct[d]
        nx = x + dx
        ny = y + dy
        # 범위 안 체크
        if -6 < nx < 6 and -6 < ny < 6:
            roads.add(((x,y), (nx,ny)))
            roads.add(((nx,ny), (x,y)))
            x = nx
            y = ny
    return len(roads)//2