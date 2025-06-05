def solution(nums: list[int], queries: list[list[int]]) -> int:
    queries.sort(key=lambda q: q[0])

    delta = [0] * (len(nums) + 1)
    inc = 0

    heap = []

    j = 0
    for i in range(len(nums)):
        inc += delta[i]

        # Consider queries starting at i and prioritize those with the
        # rightmost end points.
        while j < len(queries) and queries[j][0] == i:
            heappush(heap, -queries[j][1])
            j += 1

        # We might use queries from previous iterations which might end before
        # i (but only if not enough queries starting at i are available to
        # increment inc to nums[i]) here so we have do add the -heap[0] >= i
        # check.
        while inc < nums[i] and heap and -heap[0] >= i:
            inc += 1
            delta[-heappop(heap) + 1] -= 1

        if inc < nums[i]:
            return -1

    return len(heap)
