import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, vertex1, vertex2, weight=1):
        if 0 <= vertex1 < self.num_vertices and 0 <= vertex2 < self.num_vertices:
            self.adj_matrix[vertex1][vertex2] = weight
            self.adj_matrix[vertex2][vertex1] = weight  # For an undirected graph

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
graph = Graph(num_vertices)

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

# Visualize the graph using networkx and matplotlib
G = nx.Graph()
G.add_nodes_from(range(num_vertices))
for vertex in range(num_vertices):
    for neighbor, weight in enumerate(graph.adj_matrix[vertex]):
        if weight > 0:
            G.add_edge(vertex, neighbor)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, font_size=10, font_color='black', node_color='lightblue',
        edge_color='gray')

plt.title("Graph Representation")
plt.show()
