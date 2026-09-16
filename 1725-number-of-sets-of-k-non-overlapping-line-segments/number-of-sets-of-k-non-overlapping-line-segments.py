class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # Calculate C(n + k - 1, 2k)
        N = n + k - 1
        r = 2 * k

        ans = 1

        for i in range(1, r + 1):
            ans = ans * (N - r + i) % MOD
            ans = ans * pow(i, MOD - 2, MOD) % MOD

        return ans