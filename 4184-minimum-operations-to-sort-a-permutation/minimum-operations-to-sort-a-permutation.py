from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def get_shift(target):
            for i in range(n):
                if nums[i] == target[0]:
                    if all(nums[(i + j) % n] == target[j]
                           for j in range(n)):
                        return i
            return -1

        inc = list(range(n))
        dec = list(range(n - 1, -1, -1))

        # Check rotations of increasing order
        k = get_shift(inc)
        if k != -1:
            return min(k, (n - k) % n + 2)

        # Check rotations of decreasing order
        k = get_shift(dec)
        if k != -1:
            return min(k + 1, (n - k) % n + 1)

        return -1