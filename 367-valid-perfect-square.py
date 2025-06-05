def solution(num: int) -> bool:
    if num < 2:
        return True

    l, r = 1, num // 2
    while l <= r:
        m = l + (r - l) // 2

        tmp = m * m
        if tmp < num:
            l = m + 1
        elif tmp > num:
            r = m - 1
        else:
            return True
            
    return False
