def solution(n: int, limit: int) -> int:
    # Number of ways to choose 2 out of n objects if order does not matter.
    def helper(n):
        if n < 0:
            return 0

        return (n * (n - 1)) // 2

    # Total number of ways to distribute candies.
    c_total = helper(n + 2)
    # Ways so that at least one child get too much candy.
    c1 = 3 * helper(n - (limit + 1) + 2)
    # Ways so that at least two children get too much candy.
    c2 = 3 * helper(n - 2 * (limit + 1) + 2)
    # Ways so that at least three children get too much candy.
    c3 = helper(n - 3 * (limit + 1) + 2)

    return c_total - c1 + c2 - c3   
