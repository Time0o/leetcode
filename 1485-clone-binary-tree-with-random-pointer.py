def solution(root: 'Node' | None) -> 'NodeCopy' | None:
    if root is None:
        return None

    seen = {}

    def recurse(node):
        if node is None:
            return

        if node in seen:
            return seen[node]

        node_copy = NodeCopy(node.val)

        seen[node] = node_copy

        node_copy.left = recurse(node.left)
        node_copy.right = recurse(node.right)
        node_copy.random = recurse(node.random)

        return node_copy

    return recurse(root)
