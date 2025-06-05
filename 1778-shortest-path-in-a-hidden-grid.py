def solution(master: 'GridMaster') -> int:
    DIRECTIONS = ["U", "D", "L", "R"]
    DIRECTION_MOVE = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    DIRECTION_REVERSE = {"U": "D", "D": "U", "L": "R", "R": "L"}

    valid = {(0, 0)}
    target = None

    def dfs(r, c):
        nonlocal target

        if master.isTarget():
            target = (r, c)
            return

        for d in DIRECTIONS:
            if not master.canMove(d):
                continue

            dr, dc = DIRECTION_MOVE[d]
            r_, c_ = r + dr, c + dc
            if (r_, c_) in valid:
                continue

            valid.add((r_, c_))

            master.move(d)
            dfs(r_, c_)
            master.move(DIRECTION_REVERSE[d])

    dfs(0, 0)

    if target is None:
        return -1

    q = deque([(0, 0)])
    visited = {(0, 0)}

    res = 0
    while q:
        l = len(q)
        for _ in range(l):
            r, c = q.popleft()
            if (r, c) == target:
                return res

            for d in DIRECTIONS:
                dr, dc = DIRECTION_MOVE[d]
                r_, c_ = r + dr, c + dc
                if (r_, c_) not in valid or (r_, c_) in visited:
                    continue

                visited.add((r_, c_))
                q.append((r_, c_))

        res += 1

    assert False
