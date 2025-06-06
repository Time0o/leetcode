def solution(grid: list[list[int]]) -> int:
    n = len(grid)
 
    t_max = grid[0][0]
 
    visited = {(0, 0)}
 
    heap = [(grid[0][0], 0, 0)]
    heapify(heap)
 
    while heap:
        t, r, c = heappop(heap)
        t_max = max(t_max, t)
 
        if (r, c) == (n - 1, n - 1):
            return t_max
 
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            r_ = r + dr
            c_ = c + dc
            if r_ < 0 or r_ >= n or c_ < 0 or c_ >= n or (r_, c_) in visited:
                continue
 
            visited.add((r_, c_))
 
            heappush(heap, (grid[r_][c_], r_, c_))
            
    assert False
