def solution(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    a, b = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        a, b = b, max(a + nums[i], b)

    return b
