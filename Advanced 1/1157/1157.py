word = input().upper()
cnt = list(set(word))
a = []

for char in cnt:
    count = word.count(char)
    a.append(count)
        
if a.count(max(a)) > 1:
    print('?')
else:
    print(cnt[a.index(max(a))])
