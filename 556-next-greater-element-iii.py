def solution(n: int) -> int:
    digits = []

    tmp = n
    while tmp:
        digits.append(tmp % 10)
        tmp //= 10

    digits.reverse()

    def next_permutation(digits):
        for i in range(len(digits) - 2, -1, -1):
            if digits[i + 1] <= digits[i]:
                continue

            for j in range(len(digits) - 1, i, -1):
                if digits[j] <= digits[i]:
                    continue

                digits[i], digits[j] = digits[j], digits[i]
                digits[i+1:] = reversed(digits[i+1::])
                return True

        return False

    if not next_permutation(digits):
        return -1

    res = 0
    for d in digits:
        res = 10 * res + d
    return res if res < 2**31 else -1
