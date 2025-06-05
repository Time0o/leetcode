def solution(piles: list[int], h: int) -> int:
    l, r = (sum(piles) + h - 1) // h, max(piles)

    while l < r:
        m = l + (r - l) // 2

        if sum((p + m - 1) // m for p in piles) <= h:
            r = m
        else:
            l = m + 1

    return l
