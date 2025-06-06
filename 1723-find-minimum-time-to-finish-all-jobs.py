def solution(jobs: list[int], k: int) -> int:
    jobs.sort(reverse=True)

    res = math.inf

    def recurse(i, working_times, max_working_time):
        nonlocal res

        if i == len(jobs):
            res = max_working_time
            return

        seen = set()
        for j in range(k):
            t = working_times[j]

            if t in seen or t + jobs[i] >= res:
                continue

            seen.add(t)

            new_t = t + jobs[i]

            new_max_working_time = max(max_working_time, new_t)
            if new_max_working_time >= res:
                continue

            working_times[j] = new_t
            recurse(i + 1, working_times, new_max_working_time)
            working_times[j] = t

    recurse(0, [0] * k, 0)

    return res
