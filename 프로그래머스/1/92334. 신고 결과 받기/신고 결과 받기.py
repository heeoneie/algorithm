def solution(id_list, report, k):
    answer = []
    d = {}
    for i in id_list:
        d[i] = set()
    for r in report:
        a, b = r.split()
        d[a].add(b)
        
    cnt = {}
    for s in d.values():
        for user in s:
            if user in cnt:
                cnt[user] += 1
            else:
                cnt[user] = 1
    temp = []
    for n, c in cnt.items():
        if c >= k:
            temp.append(n)
            
    for i in d.values():
        t = 0
        for j in i:
            if j in temp:
                t += 1
        answer.append(t)
    return answer