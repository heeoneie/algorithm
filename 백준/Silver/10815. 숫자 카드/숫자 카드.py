import sys

input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))
cnt = {}

for card in cards:
    cnt[card] = 1
        
for number in numbers:
    if cnt.get(number) == 1:
        print(1, end=" ")
    else:
        print(0, end=" ")