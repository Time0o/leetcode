def solution(m: int, n: int) -> int:
    MOD = 10**9 + 7

    valid_colorings = set()

    for mask in range(3**m):
        color_prev = -1
        tmp = mask
        for _ in range(m):
            color = tmp % 3
            if color == color_prev:
                break
            color_prev = color
            tmp //= 3
        else:
            valid_colorings.add(mask)
    
    adj = defaultdict(list)
    for mask1 in valid_colorings:
        for mask2 in valid_colorings:
            tmp1, tmp2 = mask1, mask2
            for _ in range(m):
                if tmp1 % 3 == tmp2 % 3:
                    break
                tmp1 //= 3
                tmp2 //= 3
            else:
                adj[mask1].append(mask2)

    dp = [int(mask in valid_colorings) for mask in range(3**m)]

    for _ in range(1, n):
        tmp = [0] * 3**m
        for mask1 in valid_colorings:
            for mask2 in adj[mask1]:
                tmp[mask2] += dp[mask1]
                if tmp[mask2] >= MOD:
                    tmp[mask2] -= MOD
        dp = tmp

    return sum(dp) % MOD
