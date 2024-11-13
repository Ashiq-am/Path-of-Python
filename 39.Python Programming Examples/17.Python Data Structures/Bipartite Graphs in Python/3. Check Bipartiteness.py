def is_bipartite(self):
    color = {}
    for vertex in list(self.U) + list(self.V):
        if vertex not in color:
            if not self._bfs_check(vertex, color):
                return False
    return True


def _bfs_check(self, start, color):
    from collections import deque
    queue = deque([start])
    color[start] = 0  # Start coloring with color 0

    while queue:
        vertex = queue.popleft()
        current_color = color[vertex]

        for neighbor in self.adj_list[vertex]:
            if neighbor not in color:
                color[neighbor] = 1 - current_color  # Alternate color
                queue.append(neighbor)
            elif color[neighbor] == current_color:
                return False

    return True
