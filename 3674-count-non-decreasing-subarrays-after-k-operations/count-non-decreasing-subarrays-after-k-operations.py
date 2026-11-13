
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        # Next greater element
        nxt = [n] * n
        st = []

        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            if st:
                nxt[i] = st[-1]
            st.append(i)

        LOG = n.bit_length()

        jump = [nxt]
        cost = [[
            nums[i] * (nxt[i] - i) - (pref[nxt[i]] - pref[i])
            for i in range(n)
        ]]

        for j in range(1, LOG):
            prev = jump[-1]
            pc = cost[-1]

            nj = [n] * n
            nc = [0] * n

            for i in range(n):
                mid = prev[i]
                nc[i] = pc[i]

                if mid < n:
                    nj[i] = prev[mid]
                    nc[i] += pc[mid]

            jump.append(nj)
            cost.append(nc)

        def get_cost(l, r):
            total = 0
            pos = l

            for j in range(LOG - 1, -1, -1):
                p = jump[j][pos]

                if p <= r:
                    total += cost[j][pos]
                    pos = p

            total += nums[pos] * (r - pos + 1)
            total -= pref[r + 1] - pref[pos]

            return total

        # Two pointers
        ans = 0
        right = -1

        for left in range(n):
            if right < left:
                right = left

            while right + 1 < n:
                if get_cost(left, right + 1) <= k:
                    right += 1
                else:
                    break

            ans += right - left + 1

        return ans
