def solution(root: 'TreeNode' | None) -> int:
    res = 0

    def recurse(node):
        nonlocal res

        if node is None:
            return True, 0, math.inf, -math.inf

        l_bst, l_sum, l_min, l_max = recurse(node.left)
        r_bst, r_sum, r_min, r_max = recurse(node.right)

        if l_bst and r_bst and l_max < node.val < r_min:
            total_sum = l_sum + node.val + r_sum
            res = max(res, total_sum)
            return True, total_sum, min(l_min, node.val), max(r_max, node.val)
        
        # The values we return here after `False` don't matter.
        return False, 0, 0, 0

    recurse(root)

    return res
