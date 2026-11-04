from typing import List
from bisect import bisect_left

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)
        rank = {v: i + 1 for i, v in enumerate(vals)}

        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        def add(i, v, d):
            while i <= m:
                cnt[i] += d
                sm[i] += v * d
                i += i & -i

        def query(bit, i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        def kth(kth):
            idx = 0
            bit_mask = 1 << (m.bit_length() - 1)

            while bit_mask:
                nxt = idx + bit_mask
                if nxt <= m and cnt[nxt] < kth:
                    idx = nxt
                    kth -= cnt[nxt]
                bit_mask >>= 1

            return idx + 1

        def get_cost():
            mid = kth((x + 1) // 2)
            med = vals[mid - 1]

            lc = query(cnt, mid)
            ls = query(sm, mid)
            total = query(sm, m)

            return med * lc - ls + (total - ls) - med * (x - lc)

        costs = [0] * (n - x + 1)

        for i, v in enumerate(nums):
            add(rank[v], v, 1)

            if i >= x:
                old = nums[i - x]
                add(rank[old], old, -1)

            if i >= x - 1:
                costs[i - x + 1] = get_cost()

        INF = 10**18

        # DP using rolling arrays
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]