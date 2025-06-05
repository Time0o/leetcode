def solution(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])

    dp = [[0] * n for _ in range(m)]

    def dfs(r, c):
        if dp[r][c] == 0:
            path = 1
            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                r_, c_ = r + dr, c + dc
                if r_ < 0 or r_ >=m or c_ < 0 or c_ >= n:
                    continue

                if matrix[r_][c_] > matrix[r][c]:
                    path = max(path, dfs(r_, c_) + 1)

            dp[r][c] = path

        return dp[r][c]

    max_path = 0
    for r in range(m):
        for c in range(n):
            if dp[r][c] == 0:
                dfs(r, c)

            max_path = max(max_path, dp[r][c])

    return max_path
