n = int(input())
cnt = 0
res = 666

while True:
    if '666' in str(res):
        cnt += 1
    if cnt == n:
        print(res)
        break
    res += 1