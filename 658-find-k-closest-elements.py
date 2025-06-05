def solution(arr: List[int], k: int, x: int) -> List[int]:
    l, r = 0, len(arr) - k
    while l < r:
        m = (l + r) // 2
        # If arr[m] and arr[m + k] are the same this will continue
        # searching to the left if x <= arr[m].
        if x - arr[m] <= arr[m + k] - x:
            r = m
        else:
            l = m + 1

    return arr[l:l+k]
