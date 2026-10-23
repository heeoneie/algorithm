def solution(record):
    answer = []
    logs = []
    users = {}
    # 레코드 루핑 돌면서 들어온지 나간지랑 아이디 적어놓고
    for r in record:
        command = r.split(" ")[0]
        user = r.split(" ")[1]
        logs.append((user, command))
        if command == "Leave":
            continue
        else:
            nickname = r.split(" ")[2]
            users[user] = nickname
    for uid, kind in logs:
        if kind == "Enter":
            answer.append(users[uid]+"님이 들어왔습니다.")
        elif kind == "Leave":
            answer.append(users[uid]+"님이 나갔습니다.")
    return answer