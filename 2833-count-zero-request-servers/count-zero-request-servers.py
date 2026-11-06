class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a:a[1])

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        ans = [0] * len(queries)
        freq = {}
        left = 0
        right = 0

        for q , idx in sorted_queries:
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                freq[server] = freq.get(server, 0) + 1
                right += 1

            while left < right and logs[left][1] < q - x:
                server = logs[left][0]
                freq[server] -= 1

                if freq[server] == 0:
                    del freq[server]

                left += 1

            ans[idx] = n - len(freq)

        return ans
