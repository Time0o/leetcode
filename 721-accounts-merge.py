def solution(accounts: List[List[str]]) -> List[List[str]]:
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])

            return self.parent[x]

        def union(self, x, y):
            xr, yr = self.find(x), self.find(y)
            if xr == yr:
                return False

            if self.size[xr] < self.size[yr]:
                xr, yr = yr, xr

            self.parent[yr] = self.parent[xr]
            self.size[xr] += self.size[yr]

            return True

    dsu = DSU(len(accounts))

    email_to_idx = {}
    for i, account in enumerate(accounts):
        for email in account[1:]:
            if email in email_to_idx:
                dsu.union(i, email_to_idx[email])
            else:
                email_to_idx[email] = i

    accounts_merged = {}
    for email, i in email_to_idx.items():
        j = dsu.find(i)
        if j not in accounts_merged:
            accounts_merged[j] = []
        accounts_merged[j].append(email)

    return [[accounts[i][0]] + sorted(emails) for i, emails in accounts_merged.items()]
