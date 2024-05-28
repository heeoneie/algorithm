'''
30의 배수면 3의 배수면서 10의 배수
10의 배수는 일의 자리가 0
3의 배수는 각 자리 합이 3의 배수
'''
import sys

n = sys.stdin.readline().rstrip()
n = sorted(n, reverse=True)

if '0' not in n:
    print(-1)
else:
    n_sum = 0
    for i in n:
        n_sum += int(i)
    if n_sum % 3 != 0:
        print(-1)
    else:
        print(''.join(n))