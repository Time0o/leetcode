def solution(s: str, k: int) -> int:
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1

    chars_by_freq = sorted((count, c) for c, count in counts.items())

    deletions = 0

    i = 0
    while len(chars_by_freq) - i > k:
        deletions += chars_by_freq[i][0]
        i += 1

    return deletions
