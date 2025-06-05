def solution(self, arr: 'MountainArray', target: int) -> int:
    # Reduce calls to `arr.get()`
    cache = {}

    def get_cached(i):
        if i in cache:
            return cache[i]

        n = arr.get(i)
        cache[i] = n
        return n

    l, r = 0, arr.length() - 1
    while l < r:
        m = l + (r - l) // 2
        if get_cached(m) <= get_cached(m + 1):
            l = m + 1
        else:
            r = m

    peak = l
    
    l, r = 0, peak
    while l <= r:
        m = l + (r - l) // 2
        n = get_cached(m)
        if n < target:
            l = m + 1
        elif n > target:
            r = m - 1
        else:
            return m

    l, r = peak + 1, arr.length() - 1
    while l <= r:
        m = l + (r - l) // 2
        n = get_cached(m)
        if n > target:
            l = m + 1
        elif n < target:
            r = m - 1
        else:
            return m

    return -1
