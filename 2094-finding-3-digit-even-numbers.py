def solution(digits: list[int]) -> list[int]:
    counts = [0] * 10
    for d in digits:
        counts[d] += 1

    res = []

    for i in range(1, 10):
        if counts[i] == 0:
            continue
        counts[i] -= 1

        for j in range(10):
            if counts[j] == 0:
                continue
            counts[j] -= 1

            for k in range(0, 10, 2):
                if counts[k] == 0:
                    continue

                res.append(100 * i + 10 * j + k)

            counts[j] += 1

        counts[i] += 1
    
    return res
