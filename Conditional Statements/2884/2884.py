h,m = map(int,input().split())
early = 45

if m-early < 0:
    if h == 0:
        print(h+23, m+60-early)
        exit(0)
    print(h-1, m+60-early)
else:
    print(h, m-early)
