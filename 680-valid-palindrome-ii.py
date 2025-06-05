def solution(s: str) -> bool:
    def helper(i, j):
        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True

    i, j = 0, len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return helper(i + 1, j) or helper(i, j - 1)

        i += 1
        j -= 1

    return True
