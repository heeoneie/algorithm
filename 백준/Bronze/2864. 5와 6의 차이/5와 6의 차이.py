a,b = input().split() # 최솟값은 6을 다 5로 바꾸기 최댓값은 5를 다 6으로 바꾸기

a = a.replace('6','5')
b = b.replace('6','5')
min = int(a) + int(b)

a= a.replace('5','6')
b = b.replace('5','6')
max = int(a) + int(b)

print(min, max)