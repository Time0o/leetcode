def solution(nums: List[int], target: int) -> List[int]:
    res_left, res_right = None, None

    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            res_left = m
            r = m - 1

    if res_left is None:
        return [-1, -1]

    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            res_right = m
            l = m + 1

    return [res_left, res_right]      
