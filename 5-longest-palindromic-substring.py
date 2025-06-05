def solution(s: str) -> str:
    def manacher(s):
        s = "#" + "#".join(s) + "#"
        n = len(s)
        s = "$" + s+ "^"

        p = [0] * (n + 2)

        l, r = 0, 1
        for i in range(1, n + 1):
            j = l + (r - i)
            p[i] = min(r - i, p[j])

            while s[i - p[i]] == s[i + p[i]]:
                p[i] += 1

            if i + p[i] > r:
                l, r = i - p[i], i + p[i]

        p_even = [(x - 1) // 2 for x in p[1:-2:2]]
        p_odd = [x // 2 for x in p[2:-1:2]]

        return p_even, p_odd

    p_even, p_odd = manacher(s)
    max_even = max(p_even)
    max_odd = max(p_odd)

    if max_even >= max_odd:
        i = p_even.index(max_even)
        start = i - max_even
        end = i + max_even
        return s[start:end]
    else:
        i = p_odd.index(max_odd)
        start = i - max_odd + 1
        end = i + max_odd
        return s[start:end]
