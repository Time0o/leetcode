def solution(board: list[list[int]]) -> int:
    n = len(board)

    def get_pos(s):
        quot, rem = divmod(s - 1, n)
        row = n - 1 - quot  # Rows are counted from bottom

        if quot % 2 == 0:
            col = rem  # Left to right
        else:
            col = n - 1 - rem  # Right to left

        return (row, col)

    q = deque()
    q.append(1)

    visited = {1}
    
    res = 0

    while q:
        l = len(q)
        for _ in range(l):
            s = q.popleft()
            if s == n * n:
                return res

            for i in range(1, 7):
                s_ = s + i
                if s_ > n * n or s_ in visited:
                    continue

                visited.add(s_)

                r, c = get_pos(s_)
                if board[r][c] != -1 and board[r][c] not in visited:
                    s_ = board[r][c]

                visited.add(s_)

                q.append(s_)

        res += 1

    return -1
