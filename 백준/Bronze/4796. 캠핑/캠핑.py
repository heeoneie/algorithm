case = 1
while True:
    l,p,v = map(int, input().split())
    if l==0 and p==0 and v==0:
        break
    res = 0
    res = v//p * l
    if v%p <= l:
        res = res + v%p
    else:
        res = res + l
    print("Case "+str(case)+": "+str(res))
    case += 1