from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ds = [0] * numCourses
        q = deque()
        ans = []

        # 차수 구하기
        for next, prev in prerequisites:
            ds[next] += 1

        # 각 정점 번호에서 0차수인 것들 큐에 추가
        for i in range(numCourses):
            if ds[i] == 0:
                q.append(i)

        # 각 정점 번호별
        for i in range(numCourses):
            # q가 비어버리면 [] 출력
            if not q:
                return []
            # q에 있는 내용 결과에 추가
            ans.append(q.popleft())

            # 정점 탐색
            for next, prev in prerequisites:
                # 마지막 결과의 정점이랑 정점의 출발점과 같을 경우 차수를 빼준다.
                if ans[-1] == prev:
                    ds[next] -= 1
                    # 정점이 0이 되었으면 큐에 추가
                    if ds[next] == 0:
                        q.append(next)
        return ans


s = Solution()
print(s.findOrder(2, [[1, 0]]))
print(s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
