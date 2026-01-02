def bfs_s(graph, start):
    visited = set()
    result = []
    queue = [start]

    visited.add(start)

    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return result


graph = {0: [1, 3], 1: [4], 2: [1], 3: [1, 2], 4: [1]}
r = bfs_s(graph, 0)
print(r)
