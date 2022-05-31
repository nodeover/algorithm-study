# 7주차 - Wild 코드 제출
from typing import List


class Solution:
    """금주에는 풀이할 시간이 부족해서 참고용 코드를 찾아 로직을 이해하고
       주석을 정확히 써 보는 방향으로 스터디 진행하였습니다."""

    def canWork(self, blooms, days, m, k):
        flowers = 0  # 인접한 꽃 카운트를 위한 변수 선언 및 초기화
        for flower in blooms:
            flowers = flowers + 1 if (flower <= days) else 0  # 중간 기간 아래에 대해서 계산
            if flowers == k:
                m -= 1
                flowers = 0
        return m <= 0  # 0이나 음수가 나온 경우 해당 기간 이하로 가능하다는 뜻

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:  # 전체 꽃 개수 자체가 부족한 경우 short cut 으로 불가능 응답
            return -1
        left, right = 1, max(bloomDay)  # 리스트 내 꽃이 피기까지 기다려야 할 기간의 최소 최대
        while left < right:  # 최소 최대 기간을 좁히며 더이상 좁힐 수 없을 떄까지 작업 반복
            mid = (left + right) // 2
            if self.canWork(bloomDay, mid, m, k):
                right = mid
            else:
                left = mid + 1
        return left
