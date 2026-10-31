class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        right = [[-1] * n for _ in range(m)]
        down = [[-1] * n for _ in range(m)]

        # Precompute mirror destinations
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:

                    # Entering mirror while moving right
                    x, y = i + 1, j
                    if x < m:
                        if grid[x][y] == 1:
                            right[i][j] = down[x][y]
                        else:
                            right[i][j] = x * n + y

                    # Entering mirror while moving down
                    x, y = i, j + 1
                    if y < n:
                        if grid[x][y] == 1:
                            down[i][j] = right[x][y]
                        else:
                            down[i][j] = x * n + y

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                ways = dp[i][j]

                # Move right
                if j + 1 < n:
                    x, y = i, j + 1

                    if grid[x][y] == 1:
                        pos = right[x][y]
                        if pos != -1:
                            a, b = divmod(pos, n)
                            dp[a][b] = (dp[a][b] + ways) % MOD
                    else:
                        dp[x][y] = (dp[x][y] + ways) % MOD

                # Move down
                if i + 1 < m:
                    x, y = i + 1, j

                    if grid[x][y] == 1:
                        pos = down[x][y]
                        if pos != -1:
                            a, b = divmod(pos, n)
                            dp[a][b] = (dp[a][b] + ways) % MOD
                    else:
                        dp[x][y] = (dp[x][y] + ways) % MOD

        return dp[m - 1][n - 1]