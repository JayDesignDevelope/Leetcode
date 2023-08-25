import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class DiGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, from_vertex, to_vertex, weight=1):
        if 0 <= from_vertex < self.num_vertices and 0 <= to_vertex < self.num_vertices:
            self.adj_matrix[from_vertex][to_vertex] = weight

    def dfs_iterative(self, start_vertex):
        visited = set()
        stack = [start_vertex]
        dfs_result = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                dfs_result.append(vertex)
                visited.add(vertex)
                stack.extend(neighbor for neighbor, weight in enumerate(self.adj_matrix[vertex]) if
                             weight > 0 and neighbor not in visited)

        return dfs_result

    def bfs_iterative(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        bfs_result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                bfs_result.append(vertex)
                visited.add(vertex)
                queue.extend(neighbor for neighbor, weight in enumerate(self.adj_matrix[vertex]) if
                             weight > 0 and neighbor not in visited)

        return bfs_result


# Example usage
num_vertices = 4
graph = DiGraph(num_vertices)

# Adding edges
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 0)

# DFS traversal starting from vertex 0
dfs_result = graph.dfs_iterative(0)
print("DFS traversal starting from vertex 0:", dfs_result)

# BFS traversal starting from vertex 2
bfs_result = graph.bfs_iterative(2)
print("BFS traversal starting from vertex 2:", bfs_result)

# Visualize the directed graph using networkx and matplotlib
G = nx.DiGraph()
G.add_nodes_from(range(num_vertices))
for from_vertex in range(num_vertices):
    for to_vertex, weight in enumerate(graph.adj_matrix[from_vertex]):
        if weight > 0:
            G.add_edge(from_vertex, to_vertex)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, font_size=10, font_color='black', node_color='lightblue',
        edge_color='gray', arrowsize=15)

plt.title("Directed Graph Representation")
plt.show()
