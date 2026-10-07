from collections import deque

class Solution:

    def removeInvalidParentheses(self, s: str) -> list[str]:

        def isValid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = deque([s])
        visited = {s}
        result = []

        while queue:
            current = queue.popleft()

            if isValid(current):
                result.append(current)

            # If valid strings are found, don't remove more parentheses
            if result:
                continue

            for i in range(len(current)):
                if current[i] not in "()":
                    continue

                next_string = current[:i] + current[i + 1:]

                if next_string not in visited:
                    visited.add(next_string)
                    queue.append(next_string)

        return result