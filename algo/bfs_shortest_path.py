def bfs_shortest_path(graph, start, target):
    """
    Finds shortest path between two nodes using BFS.

    Returns:
        List representing the shortest path, or None if no path exists
    """
    if start == target:
        return [start]

    visited = set([start])
    queue = [(start, [start])]  # Store (node, path_to_node)

    while queue:
        node, path = queue.pop(0)  # Remove from front

        for neighbor in graph[node]:
            if neighbor not in visited:
                new_path = path + [neighbor]

                if neighbor == target:
                    return new_path

                visited.add(neighbor)
                queue.append((neighbor, new_path))  # Add to back

    return None  # No path found


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C"],
}
print(bfs_shortest_path(graph, "A", "D"))  # O(m*n)
