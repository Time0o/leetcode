def solution(n: int, intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda i: i[0])

    free_rooms = list(range(n))
    heapq.heapify(free_rooms)

    used_rooms = []
    room_usage = [0] * n

    for i in intervals:
        start = i[0]
        end = i[1]

        while used_rooms and start >= used_rooms[0][0]:
            _, room = heapq.heappop(used_rooms)
            heapq.heappush(free_rooms, room)

        if not free_rooms:
            end_, room = heapq.heappop(used_rooms)
            end = end_ + (end - start)
            heapq.heappush(free_rooms, room)

        room = heapq.heappop(free_rooms)
        room_usage[room] += 1
        heapq.heappush(used_rooms, (end, room))

    max_room_usage = max(room_usage)
    for i, u in enumerate(room_usage):
        if u == max_room_usage:
            return i

    assert False
