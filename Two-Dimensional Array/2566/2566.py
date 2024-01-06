numbers = []
rowIdx = 0
colIdx = 0

for _ in range(9):
    numbers.append(list(map(int,input().split())))
    
maxRow = [max(number) for number in numbers]
maxValue = max(maxRow)

for i, row in enumerate(numbers):
    if maxValue in row:
        rowIdx = i
        colIdx = row.index(maxValue)
        break

print(maxValue)
print(rowIdx+1,colIdx+1)
