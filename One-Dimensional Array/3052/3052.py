numbers = list()

for i in range(10):
    n = int(input())
    a = n % 42
    numbers.append(a)
    
print(len(set(numbers)))
