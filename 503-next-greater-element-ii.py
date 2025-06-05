def solution(nums: list[int]) -> list[int]:
    res = [-1] * len(nums)

    stack = nums[::-1]
    for i in range(len(nums) - 1, -1, -1):
        n = nums[i]
        while stack and stack[-1] <= n:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(n)

    return res
