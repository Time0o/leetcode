def solution(nums: list[int]) -> None:
    for i in range(len(nums) - 2, -1, -1):
        if nums[i + 1] <= nums[i]:
            continue

        for j in range(len(nums) - 1, i, -1):
            if nums[j] <= nums[i]:
                continue

            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = reversed(nums[i+1:])
            return
    
    nums.reverse()
