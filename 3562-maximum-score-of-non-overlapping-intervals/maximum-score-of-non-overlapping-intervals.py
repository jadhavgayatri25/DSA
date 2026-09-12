from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Store: (right, left, weight, original_index)
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((r, l, w, i))

        # Sort by ending position
        arr.sort()

        # Array of ending positions
        ends = [x[0] for x in arr]

        # dp[k][i] = best answer using at most k intervals
        # among the first i sorted intervals
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        def better(a, b):
            # Return the better state:
            # 1. Higher score
            # 2. If same score, lexicographically smaller indices
            if a[0] != b[0]:
                return a if a[0] > b[0] else b
            return a if a[1] < b[1] else b

        for i in range(1, n + 1):
            r, l, w, idx = arr[i - 1]

            # Number of intervals whose ending point is < l
            p = bisect_left(ends, l)

            for k in range(1, 5):
                # Option 1: don't choose current interval
                not_take = dp[k][i - 1]

                # Option 2: choose current interval
                prev_score, prev_indices = dp[k - 1][p]

                take = (
                    prev_score + w,
                    tuple(sorted(prev_indices + (idx,)))
                )

                dp[k][i] = better(not_take, take)

        return list(dp[4][n][1])