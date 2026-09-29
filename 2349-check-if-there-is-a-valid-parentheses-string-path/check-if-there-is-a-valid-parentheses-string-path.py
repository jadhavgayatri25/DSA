from functools import lru_cache

class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Path length must be even for a valid parentheses string
        if (m + n - 1) % 2 != 0:
            return False

        # First character must be '('
        if grid[0][0] == ')':
            return False

        # Last character must be ')'
        if grid[m - 1][n - 1] == '(':
            return False

        @lru_cache(None)
        def dfs(r, c, balance):

            # Process current cell
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1

            # Balance can never become negative
            if balance < 0:
                return False

            # Number of cells remaining after current cell
            remaining = (m - 1 - r) + (n - 1 - c)

            # Not enough cells left to close all '('
            if balance > remaining:
                return False

            # Reached bottom-right
            if r == m - 1 and c == n - 1:
                return balance == 0

            # Move down
            if r + 1 < m:
                if dfs(r + 1, c, balance):
                    return True

            # Move right
            if c + 1 < n:
                if dfs(r, c + 1, balance):
                    return True

            return False

        return dfs(0, 0, 0)