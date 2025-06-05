def solution(prices: list[int]) -> int:
    t_i10 = 0
    t_i11 = -math.inf

    for p in prices:
        t_i10 = max(t_i10, t_i11 + p)
        t_i11 = max(t_i11, -p)

    return t_i10
