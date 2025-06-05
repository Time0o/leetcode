def solution(s: str) -> list[str]:
    mm_left, mm_right = 0, 0
    for c in s:
        if c == "(":
            mm_left += 1
        elif c == ")":
            if mm_left == 0:
                mm_right += 1
            else:
                mm_left -= 1

    res = set()

    def recurse(i, s_modified, left, right, rem_mm_left, rem_mm_right):
        if i == len(s):
            if rem_mm_left == 0 and rem_mm_right == 0:
                res.add("".join(s_modified))
            return

        if s[i] == "(":
            if rem_mm_left > 0:
                recurse(i + 1, s_modified, left, right, rem_mm_left - 1, rem_mm_right)
        elif s[i] == ")":
            if rem_mm_right > 0:
                recurse(i + 1, s_modified, left, right, rem_mm_left, rem_mm_right - 1)

        s_modified.append(s[i])

        if s[i] != "(" and s[i] != ")":
            recurse(i + 1, s_modified, left, right, rem_mm_left, rem_mm_right)
        elif s[i] == "(":
            recurse(i + 1, s_modified, left + 1, right, rem_mm_left, rem_mm_right)
        elif s[i] == ")" and left > right:
            recurse(i + 1, s_modified, left, right + 1, rem_mm_left, rem_mm_right)

        s_modified.pop()

    recurse(0, [], 0, 0, mm_left, mm_right)

    return list(res) 
