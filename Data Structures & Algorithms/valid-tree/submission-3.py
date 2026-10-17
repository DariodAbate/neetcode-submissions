class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False] * n

        # if it is a tree, all components are connected
        visited[0] = True
        for neighbor in adj_list[0]:
            if not visited[neighbor]:
                if not self.dfs(neighbor, 0, adj_list, visited):
                    return False

        # check that all components are connected
        for v in visited:
            if not v:
                return False

        return True
    
    def dfs(self, node: int, parent: int, adj_list: List[List[int]], visited: List[int]) -> bool:
        visited[node] = True
        for neighbor in adj_list[node]:
            if neighbor == parent:
                continue 
            if visited[neighbor]:
                return False

            if not self.dfs(neighbor, node, adj_list, visited):
                return False

        return True
        

        
