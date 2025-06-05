def solution(s: str) -> int:
    curr_char = s[0]
    curr_run = 1
    max_run = 1

    for i in range(1, len(s)):
        c = s[i]
        if c == curr_char:
            curr_run += 1
            max_run = max(max_run, curr_run)
        else:
            curr_char = c
            curr_run = 1
    
    return max_run
