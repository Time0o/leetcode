def solution(words: List[str]) -> str:
    adj = defaultdict(list)
    indegree = {}

    for w in words:
        for c in w:
            indegree[c] = 0

    for i in range(len(words) - 1):
        for a, b in zip(words[i], words[i + 1]):
            if a != b:
                if b not in adj[a]:
                    adj[a].append(b)
                    indegree[b] += 1
                break
        else:
            # Handles invalid orderings like ["abc", "ab"].
            if len(words[i]) > len(words[i + 1]):
                return ""

    topological_sort = []

    q = deque([a for a, d in indegree.items() if d == 0])

    while q:
        a = q.popleft()
        topological_sort.append(a)

        for b in adj[a]:
            indegree[b] -= 1
            if indegree[b] == 0:
                q.append(b)

    if len(topological_sort) != len(indegree):
        return ""

    return "".join(topological_sort)
