def solution(graph: list[list[int]]) -> list[list[int]]:
     n = len(graph)
     
     res = []

     def dfs(node, path):
         if node == n - 1:
             res.append(path[:])
             return

         for neigh in graph[node]:
             path.append(neigh)
             dfs(neigh, path)
             path.pop()

     path = [0]
     dfs(0, path)

     return res
