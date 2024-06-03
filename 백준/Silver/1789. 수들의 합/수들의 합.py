import sys
s = int(sys.stdin.readline().rstrip())
cnt = 0
i = 0

while True:
    if s > i:
        i += 1
        s -= i
        cnt += 1
    else:
        print(cnt)
        break