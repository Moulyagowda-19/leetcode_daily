def minReorder(self, n, connections):
        graph = [[] for _ in range(n)]
        
        for u, v in connections:
            graph[u].append((v, 1))  # needs reversal if used
            graph[v].append((u, 0))  # already correctly directed towards 0
        
        visited = set()
        
        def dfs(node):
            visited.add(node)
            changes = 0
            
            for nei, direction in graph[node]:
                if nei not in visited:
                    # If direction = 1, original was node -> nei, wrong direction
                    changes += direction
                    changes += dfs(nei)
            return changes
        
        return dfs(0)