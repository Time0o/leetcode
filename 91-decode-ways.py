def solution(self, s: str) -> int:
    if s[0] == "0":
        return 0

    a, b = 1, 1
    for i in range(1, len(s)):
        new_b = 0
        # If the digit can stand on its own...
        if s[i] != "0":
            new_b += b
        j = int(s[i-1:i+1])
        # If the digit can be combined with the previous one...
        if s[i - 1] == "1" or s[i - 1] == "2" and s[i] <= "6":
            print(s[i-1:i+1])
            new_b += a

        a, b = b, new_b

    return b
