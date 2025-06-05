def solution(nums: list[int], queries: list[list[int]]) -> bool:
    delta = [0] * (len(nums) + 1)
    for a, b in queries:
        delta[a] += 1
        delta[b + 1] -= 1

    dec = 0
    for i in range(len(nums)):
        dec += delta[i]
        if dec < nums[i]:
            return False

    return True
