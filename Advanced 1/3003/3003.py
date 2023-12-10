chess = list(map(int,input().split()))
k = chess[0:2]
l = chess[2:5]
p = chess[-1]
temp = list()

for i in range(len(k)):
    temp.append(1 - k[i])
    
for i in range(len(l)):
    temp.append(2 - l[i])
    
temp.append(8-p)

for i in range(len(temp)):
    print(temp[i], end=' ')
