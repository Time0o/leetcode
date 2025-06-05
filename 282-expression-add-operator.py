def solution(self, num: str, target: int) -> List[str]:
    res = []

    def backtrack(i, expr, value, last_added):
        if i == len(num):
            if value == target:
                res.append(''.join(expr))

            return

        for j in range(i + 1, len(num) + 1):
            n_str = num[i:j]
            if len(n_str) > 1 and n_str[0] == '0':
                continue

            n = int(n_str)

            if i == 0:
                expr.append(n_str)
                backtrack(j, expr, n, n)
                expr.pop()
            else:
                expr.append('+')
                expr.append(n_str)
                backtrack(j, expr, value + n, n)
                expr.pop()
                expr.pop()

                expr.append('-')
                expr.append(n_str)
                backtrack(j, expr, value - n, -n)
                expr.pop()
                expr.pop()

                expr.append('*')
                expr.append(n_str)
                # Here we have to "undo" the last operatio such that
                # multiplication always takes precedence, this is more efficient
                # than separately parsing the whole expression at the end every
                # time.
                backtrack(j, expr, value - last_added + last_added * n, last_added * n)
                expr.pop()
                expr.pop()

    expr = []
    backtrack(0, expr, 0, 0)

    return res
