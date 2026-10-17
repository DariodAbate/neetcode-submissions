class Solution:
    VISITING = 0
    NOT_VISITED = 1
    COMPLETED = 2

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        in_degrees = [0 for _ in range(numCourses)]
        # build graph
        for a, b in prerequisites:
            in_degrees[a] += 1
            adj_list[b].append(a)

        queue = deque()
        # khan algorithm for cycle detection
        for node, in_deg in enumerate(in_degrees):
            if in_deg == 0:
                queue.append(node)

        nodes_processed = 0
        while queue:
            node = queue.popleft()
            nodes_processed += 1
            for neighbor in adj_list[node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        return nodes_processed == numCourses




        