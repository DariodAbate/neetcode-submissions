class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[]for _ in range(n)]
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False] * n

        num_conn_comps = 0
        for i in range(n):
            if not visited[i]:
                num_conn_comps += 1
                self.dfs(i, adj_list, visited)
        return num_conn_comps
    
    def dfs(self, node: int, adj_list: List[List[int]], visited: List[bool]) -> None:
        visited[node] = True

        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj_list, visited)


        