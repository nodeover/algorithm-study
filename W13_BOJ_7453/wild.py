import sys
input = sys.stdin.readline

if __name__ == "__main__":
    row_cnt = int(input())
    sum_zero_row_cnt = 0
    LIST_SUM_AB, LIST_SUM_CD = list(), list()
    mat = [list(map(int, input().split())) for _ in range(row_cnt)]

    for i in range(row_cnt):
        for j in range(row_cnt):
            LIST_SUM_AB.append(mat[i][0] + mat[j][1])
            LIST_SUM_CD.append(mat[i][2] + mat[j][3])

    LIST_SUM_AB.sort()
    LIST_SUM_CD.sort()
    LIST_SUM_CD.reverse()
    pt_ab, pt_cd = 0, 0
    arr_len = len(LIST_SUM_AB)
    while pt_ab < arr_len and pt_cd < arr_len:
        sum_ab, sum_cd = LIST_SUM_AB[pt_ab], LIST_SUM_CD[pt_cd]
        # AB합(음수) 절대값이 CD합(양수) 절대값보다 작은 경우 CD 포인터 이동
        if sum_ab + sum_cd > 0:
            pt_cd += 1
        # AB합(음수) 절대값과 CD합(양수) 절대값이 동일한 경우 합이 0인 패턴으로 감지하여 추가
        elif sum_ab + sum_cd == 0:
            sum_zero_row_cnt += 1
            # 포인터 처리 추가 필요
        # AB합(음수) 절대값이 CD합(양수) 절대값보다 작은 경우 CD 포인터 이동
        else:  # elif sum_ab + sum_cd < 0:
            pt_ab += 1

    print(sum_zero_row_cnt)
