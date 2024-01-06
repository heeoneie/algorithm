n = int(input())
m = int(input())
res = []
for i in range(n,m+1):
    if i > 1:
        num = [1]
        for j in range(2,i+1):
            if i%j == 0:
                num.append(j)
        if len(num) < 3:
            res.append(i)
if len(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(min(res))
