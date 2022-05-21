# comb 구현코드
l, c = map(int, input().split())
j = ['a', 'e', 'i', 'o', 'u']
cl = input().split()
cl.sort() # 이 정렬 한방으로 정렬조건은 만족됨.

# arr에서 length개의 원소를 뽑는 함수
# length값을 줄여가며 재귀로 조합을 구한다.
def comb(arr, length):
    res = []
    if length > len(arr):
        return res
    if length ==1:
        for i in arr:
            res.append([i])
    elif length>1:
        for i in range(len(arr) - length+1):
            for j in comb(arr[i+1:],length-1):
                res.append([arr[i]] + j)
    return res

# 조합 목록을 구해서 loop
for s in comb(cl, l):
    cnt = 0
    # 자음 카운트
    for a in j:
        if a in s:
            cnt += 1

    # 조건에 맞으면 출력
    if cnt and l - cnt >= 2:
        print(''.join(s))
