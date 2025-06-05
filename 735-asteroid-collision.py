def solution(asteroids: list[int]) -> list[int]:
    stack = []
    for a in asteroids:
        while stack and a < 0 < stack[-1]:
            if stack[-1] > -a:
                break
            if stack[-1] < -a:
                stack.pop()
            elif stack[-1] == -a:
                stack.pop()
                break
        else:
            stack.append(a)

    return stack
