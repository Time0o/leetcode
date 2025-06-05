def solution(nums: list[int]) -> list[int]:
    res = [-1] * len(nums)

    stack1, stack2 = [], []
    for i, n in enumerate(nums):
        while stack2 and nums[stack2[-1]] < n:
            res[stack2.pop()] = n

        tmp = []
        while stack1 and nums[stack1[-1]] < n:
            tmp.append(stack1.pop())

        stack2 += tmp[::-1]

        stack1.append(i)

    return res
