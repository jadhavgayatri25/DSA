class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total
        
        n = len(nums)
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        index = {value: i for i, value in enumerate(nums)}
        swaps = 0

        for i in range(n):
            while nums[i] != sorted_nums[i]:
                correct_pos = index[sorted_nums[i]]
                index[nums[i]], index[sorted_nums[i]] = correct_pos, i
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
                swaps += 1 
        return swaps       