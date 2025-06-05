def solution(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return max(nums)

    # We can only rob the first OR the last house so we can construct the
    # solution by using the house robber I algorithm on the input without the
    # first and last element respectively and returning the maximum.
    def helper(i, j):
        a, b = nums[i], max(nums[i], nums[i + 1])
        for k in range(i + 2, j + 1):
            a, b = b, max(a + nums[k], b)

        return b

    return max(helper(0, len(nums) - 2), helper(1, len(nums) - 1))
