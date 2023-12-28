t = int(input())
cents = [25,10,5,1]

for _ in range(t):
    money = int(input())
    change = []
    for cent in cents:
        change.append(money//cent)
        money = money % cent
    print(*change)
