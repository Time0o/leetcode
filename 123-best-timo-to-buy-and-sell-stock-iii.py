def solution(prices: list[int]) -> int:
    t_i10 = 0
    t_i11 = -math.inf
    t_i20 = 0
    t_i21 = -math.inf

    for p in prices:
        tmp = t_i10
        t_i10 = max(t_i10, t_i11 + p)
        t_i11 = max(t_i11, -p)
        t_i20 = max(t_i20, t_i21 + p)
        t_i21 = max(t_i21, tmp - p)

    return t_i20
