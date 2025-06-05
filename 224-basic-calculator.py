def solution(s: str) -> int:
    res = 0

    n = 0
    sgn = 1

    stack = []

    for c in s:
        if c.isdigit():
            n = n * 10 + int(c)
        elif c == "+":
            res += sgn * n
            n = 0
            sgn = 1
        elif c == "-":
            res += sgn * n
            n = 0
            sgn = -1
        elif c == "(":
            stack.append(res)
            stack.append(sgn)
            res = 0
            sgn = 1
        elif c == ")":
            res += sgn * n
            n = 0
            sgn = 1
            res *= stack.pop()
            res += stack.pop()

    return res + sgn * n
