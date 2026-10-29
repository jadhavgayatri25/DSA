class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length()
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        order = []
        timer = 0

        stack = [(0, 0, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = p
                tin[u] = timer
                timer += 1
                order.append(u)

                stack.append((u, p, 1))

                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        up = [parent[:]]

        for k in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit_idx = 0

            while diff:
                if diff & 1:
                    u = up[bit_idx][u]
                diff >>= 1
                bit_idx += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        chars = list(s)
        base = [0] * n

        for u in order:
            base[u] = (
                (base[parent[u]] if u != 0 else 0)
                ^ (1 << (ord(chars[u]) - ord('a')))
            )

        bit = [0] * (n + 2)

        def add(i, val):
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def range_xor(left, right, val):
            add(left + 1, val)
            if right + 2 <= n:
                add(right + 2, val)

        def point_query(i):
            res = 0
            i += 1

            while i > 0:
                res ^= bit[i]
                i -= i & -i

            return res

        def prefix_mask(u):
            return base[u] ^ point_query(tin[u])

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                if chars[u] != c:
                    delta = (
                        (1 << (ord(chars[u]) - ord('a')))
                        ^ (1 << (ord(c) - ord('a')))
                    )

                    range_xor(tin[u], tout[u], delta)
                    chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)

                mask = (
                    prefix_mask(u)
                    ^ prefix_mask(v)
                    ^ (1 << (ord(chars[w]) - ord('a')))
                )

                ans.append((mask & (mask - 1)) == 0)

        return ans
        