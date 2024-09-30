T = int(input())
temp = ''
a = []
for _ in range(T):
    R,S = input().split()
    R = int(R)
    for i in range(len(S)):
        temp = temp + S[i]*R
    a.append(temp)
    temp = ''
print(*a)