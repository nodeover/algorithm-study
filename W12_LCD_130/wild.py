class Solution(object):
    def solve(self, board):
        """Do not return anything, modify board in-place instead."""
        import collections
        # BFS 방식으로 'O' 표시 된 좌표들을 모두 큐에 삽입
        queue = collections.deque([])
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row in [0, len(board) - 1] or col in [0, len(board[0]) - 1]) and board[row][col] == "O":
                    queue.append((row, col))
        while queue:
            # 큐에 있는 좌표들을 넣은 순서대로 순차 처리
            row, col = queue.popleft()
            # 큐를 확장하는 방식으로 'O' 표시된 셀의 사방을 검사하고 검사된 위치는 '.' 으로 변경
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == "O":
                board[row][col] = "."
                queue.extend([(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)])
        # 인접한 곳에 'O' 표시가 없었던 경우 '.' 표시로 남게 되는 점을 이용해 보드 마킹 완성
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == ".":
                    board[row][col] = "O"
