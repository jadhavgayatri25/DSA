
from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        ans = 0

        # Check every divisor of n
        divisors = []
        d = 1
        while d * d <= n:
            if n % d == 0:
                divisors.append(d)
                if d != n // d:
                    divisors.append(n // d)
            d += 1

        for k in divisors:
            ok = True

            for i in range(0, n, k):
                block = nums[i:i + k]
                target = s[i:i + k]

                # A rotation of block must match target
                doubled = block + block[:-1]

                # KMP prefix table for target
                pi = [0] * k
                j = 0
                for x in range(1, k):
                    while j and target[x] != target[j]:
                        j = pi[j - 1]
                    if target[x] == target[j]:
                        j += 1
                    pi[x] = j

                j = 0
                found = False
                for x in range(len(doubled)):
                    while j and doubled[x] != target[j]:
                        j = pi[j - 1]
                    if doubled[x] == target[j]:
                        j += 1
                    if j == k:
                        found = True
                        break

                if not found:
                    ok = False
                    break

            if ok:
                ans += k

        return ans
