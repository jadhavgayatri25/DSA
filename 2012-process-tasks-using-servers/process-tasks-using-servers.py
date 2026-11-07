import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)

        busy = []
        ans = []
        current_time = 0

        for j, task in enumerate(tasks):
            current_time = max(current_time, j)

            # Release all available servers
            while busy and busy[0][0] <= current_time:
                time, weight, i = heapq.heappop(busy)
                heapq.heappush(free, (weight, i))

            # Wait if no server is free
            if not free:
                current_time = busy[0][0]

                while busy and busy[0][0] <= current_time:
                    time, weight, i = heapq.heappop(busy)
                    heapq.heappush(free, (weight, i))

            # Assign task to the best available server
            weight, i = heapq.heappop(free)
            ans.append(i)

            # Calculate completion time
            heapq.heappush(busy, (current_time + task, weight, i))

        return ans