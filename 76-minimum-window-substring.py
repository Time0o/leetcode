def solution(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""

    counts = {}
    for c in t:
        counts[c] = counts.get(c, 0) + 1

    counts_matched = 0

    min_window_start, min_window_end = -1, len(s)

    l = 0
    for r in range(len(s)):
        if s[r] in counts:
            counts[s[r]] -= 1
            if counts[s[r]] == 0:
                counts_matched += 1

        while counts_matched >= len(counts):
            if r - l < min_window_end - min_window_start:
                min_window_start = l
                min_window_end = r

            if s[l] in counts:
                counts[s[l]] += 1
                if counts[s[l]] == 1:
                    counts_matched -= 1
            l += 1

    if min_window_start == -1:
        return ""

    return s[min_window_start:min_window_end+1]
