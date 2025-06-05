def solution(root: TreeNode | None, target_sum: int) -> list[list[int]]:
    if root is None:
        return []

    res = []

    def dfs(node, curr_path, curr_sum):
        curr_path.append(node.val)
        curr_sum += node.val

        if node.left is None and node.right is None:
            if curr_sum == target_sum:
                res.append(curr_path[:])
        else:
            if node.left is not None:
                dfs(node.left, curr_path, curr_sum)
            if node.right is not None:
                dfs(node.right, curr_path, curr_sum)

        curr_path.pop()

    dfs(root, [], 0)

    return res
