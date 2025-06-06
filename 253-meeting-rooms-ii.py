def solution(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda i: i[0])

    # The heap contains the end times of the currently ongoing meeting
    # meetings, whenever a new one starts after one on the heap ends we can
    # evict the latter. This implies the size of the heap will never decrease
    # and so its final size is the result. 
    heap = [intervals[0][1]]
    for i in range(1, len(intervals)):
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, intervals[i][1])

    return len(heap)  
