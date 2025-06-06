def solution(events: list[list[int]]) -> int:
    events.sort(key=lambda e: e[0])

    res = 0

    i = 0
    d = 1
    heap = []
    while i < len(events) or heap:
        # If possible skip ahead.
        if i < len(events) and not heap:
            d = events[i][0]

        # Consider events starting before or on the current day.
        while i < len(events) and events[i][0] <= d:
            heapq.heappush(heap, events[i][1])
            i += 1

        # Don't consider events ending before the current day.
        while heap and heap[0] < d:
            heapq.heappop(heap)

        if heap:
            # Attend the possible event with the earliest end date on this day.
            res += 1
            heapq.heappop(heap)

        d += 1

    return res
