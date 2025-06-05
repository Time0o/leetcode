def solution(prices: list[int]) -> int:
    left = [0] * len(prices)
    min_seen = prices[0]
    for i in range(1, len(prices)):
        p = prices[i]
        left[i] = max(left[i - 1], p - min_seen)
        min_seen = min(min_seen, p)

    right = [0] * len(prices)
    max_seen = prices[-1]
    for i in range(len(prices) - 2, -1, -1):
        p = prices[i]
        right[i] = max(right[i + 1], max_seen - p)
        max_seen = max(max_seen, p)

    max_profit = 0
    for i in range(0, len(prices) - 1):
        max_profit = max(max_profit, left[i] + right[i + 1])
    return max(max_profit, left[-1])
