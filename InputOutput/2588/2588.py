a = int(input())
b = list(map(int, str(input())))
temp = 0
res = 0
mul = 1

for i in range(len(b)-1,-1,-1):
    temp = a*b[i]
    print(temp)
    temp = temp*mul
    mul = mul*10
    res = res + temp
    temp = 0
print(res)
