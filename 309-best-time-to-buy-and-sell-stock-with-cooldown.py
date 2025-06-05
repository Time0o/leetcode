def solution(prices: list[int]) -> int:
    t_i0 = 0
    t_i1 = -math.inf

    t_i0_prev = 0
    for p in prices:
        tmp = t_i0
        t_i0 = max(t_i0, t_i1 + p)
        t_i1 = max(t_i1, t_i0_prev - p)
        t_i0_prev = tmp

    return t_i0
