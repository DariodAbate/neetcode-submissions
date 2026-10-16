class Solution:
    VISITING = 0
    NOT_VISITED = 1
    COMPLETED = 2

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        # build graph
        for a, b in prerequisites:
            adj_list[b].append(a)

        # dfs with cycle detection
        state = [self.NOT_VISITED] * numCourses
        for node in range(numCourses):
            if state[node] == self.NOT_VISITED:
                if not self.dfs(node, adj_list, state):
                    return False

        return True
            

    def dfs(self, node, adj_list, state) -> bool:
        state[node] = self.VISITING
        for neighbor in adj_list[node]:
            if state[neighbor] == self.VISITING: # back edge
                return False
            if state[neighbor] == self.NOT_VISITED:
                if not self.dfs(neighbor, adj_list, state):
                    return False                       

        state[node] = self.COMPLETED
        return True




        