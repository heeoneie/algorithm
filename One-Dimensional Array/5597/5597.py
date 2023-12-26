stu = [i for i in range(1,31)]

for _ in range(28):
    fin = int(input())
    stu.remove(fin)
    
print(min(stu))
print(max(stu))
