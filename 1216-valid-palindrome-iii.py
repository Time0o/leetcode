def solution(s: str, k: int) -> bool:
    n = len(s)

    dp = [0] * n

    for i in range(n - 1, -1, -1):
        dp[i] = 1

        dp_j_prev = 0
        for j in range(i + 1, n):
            dp_j = dp[j]
            if s[i] == s[j]:
                dp[j] = dp_j_prev + 2
            else:
                dp[j] = max(dp[j - 1], dp[j])
            dp_j_prev = dp_j

    return n - dp[-1] <= k
