class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses

        # b before a
        for a, b in prerequisites:
            adj_list[b].append(a)
            in_degrees[a] +=1

        # kahn algorithm
        queue = deque()
        for node in range(numCourses):
            if in_degrees[node] == 0:
                queue.append(node)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in adj_list[node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(res) != numCourses:
            return []
        else:
            return res


        