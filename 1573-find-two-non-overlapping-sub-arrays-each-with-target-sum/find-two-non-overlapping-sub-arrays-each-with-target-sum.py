class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # best[i] = minimum length of a valid subarray
        # ending at or before index i
        best = [float('inf')] * n

        left = 0
        curr_sum = 0
        ans = float('inf')
        min_len = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            # Since all arr[i] are positive, use sliding window
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # Check if there is a previous non-overlapping subarray
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, length + best[left - 1])

                min_len = min(min_len, length)

            # Store the best subarray found up to this index
            if right == 0:
                best[right] = min_len
            else:
                best[right] = min(best[right - 1], min_len)

        return -1 if ans == float('inf') else ans