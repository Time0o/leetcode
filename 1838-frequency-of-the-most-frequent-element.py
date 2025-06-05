def solution(nums: list[int], k: int) -> int:
    nums.sort()

    res = 0

    curr_sum = 0

    l = 0
    for r in range(len(nums)):
        curr = nums[r]
        curr_sum += nums[r]

        while (r - l + 1) * curr - curr_sum > k:
            curr_sum -= nums[l]
            l += 1

        res = max(res, r - l + 1)

    return res
