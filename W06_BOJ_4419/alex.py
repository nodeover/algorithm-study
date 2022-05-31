N = int(input())
names = [input().rstrip() for _ in range(N)]
ballots = []
candidates = [True] * N
 
for _ in range(1000):
    try:
        l = list(map(lambda x: int(x) - 1, input().split()))[::-1]
        ballots.append(l)
    except Exception as e:
        break
 
# 과반 기준
half = len(ballots) // 2 + 1
 
# 계산
while True:
    votes = [0] * N
    for b in ballots:  # 유권자 표 검사
        while not candidates[b[-1]]:  # 탈락자 표 삭제
            b.pop()
        votes[b[-1]] += 1  # 득표 계산
 
    max_val = max(votes)
 
    if max_val >= half:
        for i in range(len(votes)):
            if votes[i] == max_val:
                print(names[i])
        break
 
    min_val = max_val
    for i, v in enumerate(votes):
        if candidates[i]:
            min_val = min(v, min_val)
 
    if min_val == max_val:
        for i in range(len(votes)):
            if votes[i] == max_val:
                print(names[i])
        break
 
    cnt = 0
    for i in range(len(votes)):
        if candidates[i] and votes[i] == min_val:
            cnt += 1
            candidates[i] = False
    if cnt == 0:
        for i in range(len(votes)):
            if votes[i] == max_val:
                print(names[i])
        break
        