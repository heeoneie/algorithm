a,b = map(int, input().split())
c = int(input())

if b+c >= 60:
    if a+(b+c)//60 >= 24:
        print((a-24)+(b+c)//60, (b+c)%60)
        exit()
    print(a+(b+c)//60,(b+c)%60)
else:
    print(a,b+c)
