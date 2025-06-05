def solution(k: int, prices: list[int]) -> int:
    # If k >= n // 2 we could optimize this by applying the solution for k
    # = inf (since more meaningful transactions are not possible).

    t_ik0 = [0] * (k + 1)
    t_ik1 = [-math.inf] * (k + 1)

    for p in prices:
        for j in range(k, 0, -1):
            t_ik0[j] = max(t_ik0[j], t_ik1[j] + p)
            t_ik1[j] = max(t_ik1[j], t_ik0[j - 1] - p)

    return t_ik0[-1]
