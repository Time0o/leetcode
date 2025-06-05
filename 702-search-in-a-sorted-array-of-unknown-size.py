def solution(reader: 'ArrayReader', target: int) -> int:
    # Since the secret array is ascending and all its elements are unique,
    # the maximum index at which target might be found is `target -
    # reader.get(0)`.
    l, r = 0, target - reader.get(0)

    while l <= r:
        m = l + (r - l) // 2
        n = reader.get(m)
        if n < target:
            l = m + 1
        elif n > target:
            r = m - 1
        else:
            return m

    return -1
