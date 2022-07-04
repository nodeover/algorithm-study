from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        q = []
        d = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        # top/bottom
        for a in range(0, n):
            if board[0][a] == 'O':
                board[0][a] = '*'
                q.append([0, a])
            if board[m - 1][a] == 'O':
                board[m - 1][a] = '*'
                q.append([m - 1, a])

        # left/right
        for a in range(0, m):
            if board[a][0] == 'O':
                board[a][0] = '*'
                q.append([a, 0])
            if board[a][n - 1] == 'O':
                board[a][n - 1] = '*'
                q.append([a, n - 1])

        # check boundary
        # print(q)
        while q:
            cur_d = q.pop()
            for d_d in d:
                x = cur_d[0] + d_d[0]
                y = cur_d[1] + d_d[1]
                if x >= 0 and x < m and y >= 0 and y < n and board[x][y] == 'O':
                    board[x][y] = '*'
                    q.append([x, y])

        for x in range(m):
            for y in range(n):
                if board[x][y] == '*':
                    board[x][y] = 'O'
                elif board[x][y] == 'O':
                    board[x][y] = 'X'

        return board


s = Solution()
res = s.solve([
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]])
sol = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
if res != sol:
    print('FAIL: ', res)
else:
    print('PASS')
