def solution(nums: list[int], queries: list[list[int]]) -> int:
    delta = [0] * (len(nums) + 1)
    diff = 0

    j = 0
    for i in range(len(nums)):
        while diff + delta[i] < nums[i]:
            if j == len(queries):
                return -1

            a, b, v = queries[j]
            if b >= i:
                delta[max(a, i)] += v
                delta[b + 1] -= v

            j += 1

        diff += delta[i]

    return j
