def solution(nums: List[int]) -> bool:
    s = sum(nums)
    if s % 2 == 1:
        return False

    target = s // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for n in nums:
        for t in range(target, n - 1, -1):
            dp[t] = dp[t] or dp[t - n]

    return dp[target]
