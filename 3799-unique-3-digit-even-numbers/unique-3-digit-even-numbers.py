class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        count = 0

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    
                    # Each copy can be used only once
                    if i == j or j == k or i == k:
                        continue
                    
                    # First digit cannot be 0
                    if digits[i] == 0:
                        continue
                    
                    # Last digit must be even
                    if digits[k] % 2 != 0:
                        continue
                    
                    count += 1

        # Need distinct numbers, so use a set
        numbers = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or j == k or i == k:
                        continue
                    if digits[i] == 0:
                        continue
                    if digits[k] % 2 != 0:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    numbers.add(num)

        return len(numbers)