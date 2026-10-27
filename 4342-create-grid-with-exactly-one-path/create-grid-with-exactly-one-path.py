class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]

        i, j = 0, 0
        grid[i][j] = '.'

        while j < n - 1:
            grid[i][j + 1] = '.'
            j += 1

            if i + 1 < m and j < n - 1:
                i += 1
                grid[i][j] = '.'

        while i < m - 1:
            i += 1
            grid[i][j] = '.'

        return [''.join(row) for row in grid]