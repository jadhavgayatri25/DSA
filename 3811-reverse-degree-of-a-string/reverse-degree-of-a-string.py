class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0

        for i, ch in enumerate(s, 1):
            reverse_value = 26 - (ord(ch) - ord('a'))
            total += reverse_value * i

        return total 