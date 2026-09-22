class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # Each node = (product of segment, prefix-count array)
        # prefix-count[r] = number of prefixes having product % k == r

        size = 1
        while size < n:
            size *= 2

        prod = [1] * (2 * size)
        pref = [[0] * k for _ in range(2 * size)]

        # Build leaves
        for i in range(n):
            p = nums[i] % k
            prod[size + i] = p
            pref[size + i][p] = 1

        # Empty leaves
        for i in range(n, size):
            prod[size + i] = 1

        # Merge two nodes
        def merge(a_prod, a_pref, b_prod, b_pref):
            new_prod = (a_prod * b_prod) % k
            new_pref = a_pref[:]

            for r in range(k):
                new_pref[(a_prod * r) % k] += b_pref[r]

            return new_prod, new_pref

        # Build tree
        for i in range(size - 1, 0, -1):
            prod[i], pref[i] = merge(
                prod[i * 2],
                pref[i * 2],
                prod[i * 2 + 1],
                pref[i * 2 + 1]
            )

        # Point update
        def update(pos, value):
            idx = size + pos

            value %= k
            prod[idx] = value
            pref[idx] = [0] * k
            pref[idx][value] = 1

            idx //= 2

            while idx:
                prod[idx], pref[idx] = merge(
                    prod[idx * 2],
                    pref[idx * 2],
                    prod[idx * 2 + 1],
                    pref[idx * 2 + 1]
                )
                idx //= 2

        # Query range [left, right]
        def query(left, right):
            left += size
            right += size + 1

            # Identity node
            left_prod = 1
            left_pref = [0] * k

            right_prod = 1
            right_pref = [0] * k

            while left < right:
                if left & 1:
                    left_prod, left_pref = merge(
                        left_prod,
                        left_pref,
                        prod[left],
                        pref[left]
                    )
                    left += 1

                if right & 1:
                    right -= 1

                    right_prod, right_pref = merge(
                        prod[right],
                        pref[right],
                        right_prod,
                        right_pref
                    )

                left //= 2
                right //= 2

            # Important: left part comes before right part
            return merge(
                left_prod,
                left_pref,
                right_prod,
                right_pref
            )

        ans = []

        for index, value, start, x in queries:
            # Persistent update
            update(index, value)

            # All possible remaining arrays are prefixes
            # of nums[start ... n-1]
            _, prefix_count = query(start, n - 1)

            ans.append(prefix_count[x])

        return ans 