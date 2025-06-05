def solution(self, nums1: List[int], nums2: List[int]) -> float:
    # Operating on the smaller array reduces the time complexity.
    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)

    # `r` is *inclusive* here because `i = m` is a valid partition where all
    # elements of `nums1` are in the combined left half.
    l, r = 0, m
    while l <= r:
        # Partition of `nums1`
        i = l + (r - l) // 2
        # Corresponding partition of `nums1` so that half (rounded up) of all
        # elements lie in the combined left half
        j = (m + n + 1) // 2 - i

        left1 = -inf if i == 0 else nums1[i - 1]
        left2 = -inf if j == 0 else nums2[j - 1]
        right1 = inf if i == m else nums1[i]
        right2 = inf if j == n else nums2[j]

        left_max = max(left1, left2)
        right_min = min(right1, right2)

        if left_max <= right_min:
            if (m + n) % 2 == 0:
                return (left_max + right_min) / 2
            else:
                return left_max
        # We are only moving index `i` into `nums1` and want all numbers in the
        # resulting combined left half to be smaller than all numbers in the
        # combined right half. If `nums1[i - 1]` is larger than `nums2[j]` we
        # have moved `i` too far.
        elif left1 > right2:
            r = i - 1
        else:
            l = i + 1
