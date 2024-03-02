import sys
from collections import deque

n = int(sys.stdin.readline())
card = deque(i for i in range(1,n+1))

while len(card) != 1:
    card.popleft()
    card.rotate(-1)
    
print(card[0])