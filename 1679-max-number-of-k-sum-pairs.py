def solution(nums: list[int], k: int) -> int:
    res = 0

    avail = defaultdict(int)
    for n in nums:
        if avail[k - n] > 0:
            res += 1
            avail[k - n] -= 1
        else:
            avail[n] += 1

    return res
