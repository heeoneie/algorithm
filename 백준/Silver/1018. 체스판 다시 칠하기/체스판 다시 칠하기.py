import sys
input = sys.stdin.readline
n,m = map(int, input().split())
board = [input() for _ in range(n)]
repaint = []

for i in range(n-7):
    for j in range(m-7):
        white = 0
        black = 0
        for y in range(i,i+8):
            for x in range(j,j+8):
                if (x+y) % 2 == 0:
                    if board[y][x] != 'W':
                        white += 1
                    else:
                        black += 1
                else:
                    if board[y][x] != 'W':
                        black += 1
                    else:
                        white += 1
        repaint.append(white)
        repaint.append(black)
print(min(repaint))
            