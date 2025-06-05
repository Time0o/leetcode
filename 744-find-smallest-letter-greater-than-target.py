def solution(letters: List[str], target: str) -> str:
    # We have to make r exlusive here so that we can return the first character
    # if l == len(letters), indicating no character > target has been found.
    l, r = 0, len(letters)
    while l < r:
        m = l + (r - l) // 2
        if letters[m] > target:
            r = m
        else:
            l = m + 1

    return letters[l % len(letters)]
