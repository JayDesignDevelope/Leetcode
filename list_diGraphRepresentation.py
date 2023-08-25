import networkx as nx
import matplotlib.pyplot as plt

class DiGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.adj_list and to_vertex in self.adj_list:
            self.adj_list[from_vertex].append(to_vertex)

    def dfs_iterative(self, start_vertex):
        visited = set()
        stack = [start_vertex]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                stack.extend(neighbor for neighbor in self.adj_list[vertex] if neighbor not in visited)

    def bfs_iterative(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

# Example usage
graph = DiGraph()

# Adding vertices and edges...
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")

# DFS traversal starting from vertex "A"
print("DFS traversal starting from vertex A:")
graph.dfs_iterative("A")
print()

# BFS traversal starting from vertex "C"
print("BFS traversal starting from vertex C:")
graph.bfs_iterative("C")
print()

# Visualize the directed graph using networkx and matplotlib
G = nx.DiGraph()
G.add_nodes_from(graph.adj_list.keys())
for from_vertex, to_vertices in graph.adj_list.items():
    for to_vertex in to_vertices:
        G.add_edge(from_vertex, to_vertex)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, font_size=20, font_color='black', node_color='lightblue', edge_color='gray', arrowsize=15)

plt.title("Directed Graph Representation")
plt.show()
