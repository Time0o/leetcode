def solution(rec1: list[int], rec2: list[int]) -> bool:
    x11, y11, x21, y21 = rec1
    x12, y12, x22, y22 = rec2

    return not (x12 >= x21 or x22 <= x11 or y12 >= y21 or y22 <= y11)
