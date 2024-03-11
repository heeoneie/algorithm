import sys

input= sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))
count = {}

for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1
        
for number in numbers:
    res = count.get(number)
    if res == None:
        print(0, end=" ")
    else:
        print(res, end=" ")