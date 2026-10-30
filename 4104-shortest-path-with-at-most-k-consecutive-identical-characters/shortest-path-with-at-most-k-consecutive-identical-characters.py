from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))

        pq = [(0, 0, labels[0], 1)]
        dist = {(0, labels[0], 1): 0}

        while pq:
            cost, node, last, count = heapq.heappop(pq)

            if cost != dist[(node, last, count)]:
                continue

            if node == n - 1:
                return cost

            for nei, weight in graph[node]:
                ch = labels[nei]

                if ch == last:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + weight
                state = (nei, ch, new_count)

                if new_cost < dist.get(state, float('inf')):
                    dist[state] = new_cost
                    heapq.heappush(
                        pq, (new_cost, nei, ch, new_count)
                    )

        return -1