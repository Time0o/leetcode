def solution(events: list[list[int]], k: int) -> int:
    events.sort(key=lambda e: e[1])

    dp = [[events[0][2]] * k for _ in events]

    for i in range(1, len(events)):
        start, end, v = events[i]

        l, r = 0, i
        while l < r:
            m = l + (r - l) // 2
            if events[m][1] < start:
                l = m + 1
            else:
                r = m

        # Index of last event ending before this one starts.
        i_ = l - 1

        for j in range(k):
            tmp = v + dp[i_][j - 1] if j > 0 and i_ != -1 else v
            dp[i][j] = max(dp[i - 1][j], tmp) 

    return dp[-1][-1]
