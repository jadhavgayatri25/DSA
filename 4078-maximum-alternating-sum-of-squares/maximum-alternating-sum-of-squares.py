class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x:x * x)

        n = len(nums)
        ans = 0

        for i in range(n):
            if i< n // 2:
                ans -= nums[i] * nums[i]
            else:
                ans += nums[i] * nums[i]

        return ans
