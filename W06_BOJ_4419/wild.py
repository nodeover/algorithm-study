import sys
sysinput = sys.stdin.readline

# 후보자 입력
candidates_cnt = int(sysinput())
if candidates_cnt == 0:
    raise ValueError("There is no candidate")
candidates = [sysinput().strip() for i in range(candidates_cnt)]

# 투표지 입력
ballots = dict()
ballot = [int(num) for num in sysinput().split()]
if not ballot:
    raise ValueError("There is no ballot")
ballot_idx = 0
while ballot:
    ballots[ballot_idx] = ballot
    ballot_idx += 1
    ballot = [int(num) for num in sysinput().split()]
ballots_cnt = len(ballots)
ballot_cursors = [0 for _ in range(ballots_cnt)]

# 후보자별 득표 카운트
vote_cnt_per_candidate = [int() for j in range(candidates_cnt)]
# 후보자별 투표지 확보 리스트(set)
ballots_per_candidate = [set() for j in range(candidates_cnt)]
# 탈락자 리스트
eliminated_candidates_idx = []

# 개표 진행
remaining_candidates_idx = [i for i in range(candidates_cnt)]
ballots_to_count = ballots.keys()
while True:
    # 1. 개표 라운드 진행
    for ballot_idx in ballots_to_count:
        # 투표지 확인
        ballot = ballots[ballot_idx]
        voted_to = ballot[ballot_cursors[ballot_idx]] - 1
        # #### 투표 대상이 탈락한 후보인 경우 후순위 조회
        if voted_to not in remaining_candidates_idx:
            for _ in range(ballot_cursors[ballot_idx], len(ballot)):
                ballot_cursors[ballot_idx] += 1
                voted_to = ballot[ballot_cursors[ballot_idx]] - 1
                if voted_to in remaining_candidates_idx:
                    break  # 후순위 랭크에서 남은 후보 번호가 나온 경우 카운트 기록
        # #### 유효한 후보자에 대해 득표 카운트 및 투표용지 번호 기록
        if ballots_per_candidate[voted_to] is not None:
            vote_cnt_per_candidate[voted_to] += 1
            ballots_per_candidate[voted_to].add(ballot_idx)

    # 2. 개표 라운드 결과 해석
    # A. 과반 득표자가 나온 경우
    max_vote_cnt = max(vote_cnt_per_candidate)
    if max_vote_cnt > ballots_cnt/2:
        # print(max_vote_cnt, ballots_cnt/2)
        winners_idx = [vote_cnt_per_candidate.index(max_vote_cnt)]
        break

    # B. 과반 득표자가 없는 경우
    # #### 최소득표자 카운트
    min_vote_cnt = 1001
    min_voted_candidates = []
    for vote_cnt, candidate_idx in zip(vote_cnt_per_candidate, range(candidates_cnt)):
        if vote_cnt != -1:
            if vote_cnt < min_vote_cnt:
                min_vote_cnt = vote_cnt
                min_voted_candidates = [candidate_idx]
            elif vote_cnt == min_vote_cnt:
                if not min_voted_candidates:
                    raise RuntimeError("candidate_vote_cnt cannot be equal to the initial value {}".format(min_vote_cnt))
                min_voted_candidates.append(candidate_idx)
    # print(max_vote_cnt, min_vote_cnt, min_voted_candidates)

    # #### 남은 후보자 전원 동률인 경우 종료
    if min_vote_cnt == max_vote_cnt:
        winners_idx = remaining_candidates_idx
        break

    # #### 탈락자가 있는 경우
    # 1) 탈락자 식별 및 남은 후보자 리스트에서 제거
    for candidate_idx in min_voted_candidates:
        remaining_candidates_idx.pop(remaining_candidates_idx.index(candidate_idx))

    # 2) 탈락자가 취득한 표를 다음 라운드 진행을 위해 통합
    ballots_to_count = set()
    for candidate_idx in min_voted_candidates:
        if ballots_per_candidate[candidate_idx] is not None:
            ballots_to_count = ballots_to_count.union(ballots_per_candidate[candidate_idx])
        # 2-1) 탈락자 득표 카운트 및 리스트 제거
        vote_cnt_per_candidate[candidate_idx] = -1
        ballots_per_candidate[candidate_idx] = None
    # 3) 탈락자가 가졌던 표에 대해 카운트할 커서 위치 이동
    for ballot_idx in ballots_to_count:
        ballot_cursors[ballot_idx] += 1

for i in winners_idx:
    print(candidates[i])
