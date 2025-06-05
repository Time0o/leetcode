import math

def solution(coins: List[int], amount: int) -> int:
    dp = [math.inf] * (amount + 1)
    dp[0] = 0

    for c in coins:
        for a in range(c, amount + 1):
            dp[a] = min(dp[a], dp[a - c] + 1)

    return dp[-1] if dp[-1] != math.inf else -1
