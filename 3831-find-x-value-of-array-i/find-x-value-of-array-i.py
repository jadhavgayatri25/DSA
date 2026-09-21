class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        
        # dp[r] = number of subarrays ending at previous position
        # whose product % k == r
        dp = [0] * k
        
        for num in nums:
            val = num % k
            new_dp = [0] * k
            
            # Start a new subarray with only nums[i]
            new_dp[val] += 1
            
            # Extend all previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * val) % k
                    new_dp[new_r] += dp[r]
            
            dp = new_dp
            
            # Add all subarrays ending at current position
            for r in range(k):
                ans[r] += dp[r]
        
        return ans