def solution(cost: List[int]) -> int:
    a, b = cost[-2], cost[-1]
    for i in range(len(cost) - 3, -1, -1):
        a, b = cost[i] + min(a, b), a

    return min(a, b) 
