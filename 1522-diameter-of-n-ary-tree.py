def solution(root: 'Node') -> int:
    res = 0

    def recurse(node):
        nonlocal res

        heights = [recurse(c) for c in node.children]

        if not heights:
            return 1

        heights.sort()

        if len(heights) == 1:
            diam = heights[-1]
        else:
            diam = heights[-1] + heights[-2]

        res = max(res, diam)

        return heights[-1] + 1

    recurse(root)

    return res
