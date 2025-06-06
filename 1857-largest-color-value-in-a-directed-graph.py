def solution(self, colors: str, edges: list[list[int]]) -> int:
    def topological_sort(n, adj):
        indegree = [0] * n

        for a in adj:
            for b in adj[a]:
                indegree[b] += 1

        q = deque([a for a in range(n) if indegree[a] == 0])

        topological_sort = []

        while q:
            a = q.popleft()
            topological_sort.append(a)

            for b in adj[a]:
                indegree[b] -= 1
                if indegree[b] == 0:
                    q.append(b)

        if len(topological_sort) != n:
            return False, []

        return True, topological_sort

    n = len(colors)

    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
    
    cycle_free, ts = topological_sort(n, adj)
    if not cycle_free:
        return -1

    dp = [[0] * 26 for _ in range(n)]

    res = 0

    for a in ts:
        c = ord(colors[a]) - ord("a")
        dp[a][c] += 1
        res = max(res, dp[a][c])

        for b in adj[a]:
            for c in range(26):
                dp[b][c] = max(dp[b][c], dp[a][c])

    return res
