def solution(nums: List[int]) -> int:
    houses = [0] * (max(nums) + 1)
    for n in nums:
        houses[n] += n

    a, b = houses[0], max(houses[0], houses[1])
    for i in range(2, len(houses)):
        a, b = b, max(a + houses[i], b)
    return b
