import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))
a.sort()

for number in numbers:
    start, end = 0, n-1
    isExist = False
    
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == number:
            isExist = True
            print(1)
            break
        elif a[mid] > number:
            end = mid - 1
        else:
            start = mid + 1
            
    if not isExist:
        print(0)