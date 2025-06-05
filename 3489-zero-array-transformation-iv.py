def solution(nums: list[int], queries: list[list[int]]) -> int:
    if all(n == 0 for n in nums):
        return 0

    # The ith bit in b[j] indicates whether the number i can be constructed
    # from the queries seen so far.
    b = [1] * len(nums)

    for i, (a, b, v) in enumerate(queries):
        for j in range(a, b + 1):
            p[j] |= p[j] << v

        for j, n in enumerate(nums):
            if (p[j] & (1 << n)) == 0:
                break
        else:
            return i + 1

    return -1
