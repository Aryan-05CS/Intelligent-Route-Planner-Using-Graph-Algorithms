def dfs(graph, start):

    visited = set()
    traversal = []

    def helper(node):

        visited.add(node)
        traversal.append(node)

        for neighbor, _ in graph[node]:

            if neighbor not in visited:
                helper(neighbor)

    helper(start)

    return traversal