def solution(prices: list[int]) -> int:
    t_i0 = 0
    t_i1 = -math.inf

    for p in prices:
        tmp = t_i0
        t_i0 = max(t_i0, t_i1 + p)
        t_i1 = max(t_i1, tmp - p)

    return t_i0
