# We solve this greedily.
def solution(root: Optional[TreeNode]) -> int:
    HAS_CAMERA = 0
    IS_COVERED = 1
    NEEDS_COVERAGE = 2

    num_cameras = 0

    def recurse(node):
        nonlocal num_cameras

        l = recurse(node.left) if node.left else IS_COVERED
        r = recurse(node.right) if node.right else IS_COVERED

        if l == NEEDS_COVERAGE or r == NEEDS_COVERAGE:
            num_cameras += 1
            return HAS_CAMERA

        return IS_COVERED if l == HAS_CAMERA or r == HAS_CAMERA else NEEDS_COVERAGE

    if recurse(root) == NEEDS_COVERAGE:
        num_cameras += 1

    return num_cameras
