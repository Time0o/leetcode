def solution(nums: List[int], target: int) -> int:
    # The result does not depend on the sign of target and we want to find a
    # partition into subsets s1, s2 such that sum(s1) - sum(s2) = target and
    # sum(s1) + sum(s2) = target, hence this rather unintuitive calculation.
    target = abs(target) + sum(nums)
    if target % 2 != 0:
        return 0
    target //= 2

    dp = [1] + [0] * target

    for n in nums:
        for t in range(target, n - 1, -1):
            dp[t] += dp[t - n]

    return dp[-1]
