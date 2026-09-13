class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ans = 0

        # Try every possible translation
        for dr in range(-n + 1, n):
            for dc in range(-n + 1, n):
                overlap = 0

                for i in range(n):
                    for j in range(n):
                        ni = i + dr
                        nj = j + dc

                        # Check if translated position is inside img2
                        if 0 <= ni < n and 0 <= nj < n:
                            if img1[i][j] == 1 and img2[ni][nj] == 1:
                                overlap += 1

                ans = max(ans, overlap)

        return ans