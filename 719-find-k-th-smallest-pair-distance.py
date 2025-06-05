def solution(nums: List[int], k: int) -> int:
    # Sort array so we can efficiently count pairs with distance less than or
    # equal to some specific distance via a sliding window later on.
    nums.sort()

    # Find smallest distance such that >= `k` pairs have a distance less than
    # or equal to that distance.
    l, r = 0, nums[-1] - nums[0]
    while l < r:
        m = l + (r - l) // 2

        num_pairs = 0

        # Count number of pairs with distance <= `m`.
        i = 0
        for j in range(len(nums)):
            while nums[j] - nums[i] > m:
                i += 1

            num_pairs += j - i

        if num_pairs >= k:
            r = m
        else:
            l = m + 1

    return l
