def solution(arr: list[int]) -> bool:
    odd_count = 0
    for n in arr:
        if n % 2 == 1:
            odd_count += 1
            if odd_count == 3:
                return True
        else:
            odd_count = 0

    return False
