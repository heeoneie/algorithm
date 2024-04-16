self_num = set(range(1,10001))
creator_num = set()
# 1부터 1만까지 루프 돌리면서 생성자 숫자를 집합에 넣음
# 루프가 끝나면 self_num 집합에서 creator_num 집합을 빼고 출력
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    creator_num.add(i)
        
self_num = self_num - creator_num
for num in sorted(self_num):
    print(num)