def solution(s: str) -> bool:
    defects = 0

    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            defects += 1
            if defects > 2:
                return False

        i += 1
        j -= 1

    return True
