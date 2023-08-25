from collections import deque

import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)  # For an undirected graph

    def dfs_iterative(self, start_vertex):
        visited = set() #O(V)
        stack = [start_vertex] #O(V)
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                # stack.extend(neighbor for neighbor in self.adj_list[vertex] if neighbor not in visited)
                for neighbor in self.adj_list[vertex]:
                    if neighbor not in visited:
                        stack.extend(neighbor)


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

    def has_cycle_bfs(self):
        visited = set()
        for vertex in self.adj_list:
            if vertex not in visited:
                if self.detect_cycle_bfs(vertex, visited):
                    return True
        return False

    def detect_cycle_bfs(self, start_vertex, visited):
        queue = deque()
        parent = {}

        queue.append(start_vertex)
        visited.add(start_vertex)
        parent[start_vertex] = None

        while queue:
            current_vertex = queue.popleft()

            for neighbor in self.adj_list[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = current_vertex
                elif parent[current_vertex] != neighbor:
                    return True

        return False

# Example usage
graph = Graph()

# Adding vertices and edges...
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")

#Formed Graph
print("Graph Representation")
print(graph.adj_list)


# DFS traversal starting from vertex "A"
print("DFS traversal starting from vertex C:")
graph.dfs_iterative("C")
print()

# BFS traversal starting from vertex "C"
print("BFS traversal starting from vertex C:")
graph.bfs_iterative("C")
print()
print(graph.has_cycle_bfs())

# Visualize the graph using networkx and matplotlib
G = nx.Graph()
G.add_nodes_from(graph.adj_list.keys())
for vertex, neighbors in graph.adj_list.items():
    for neighbor in neighbors:
        G.add_edge(vertex, neighbor)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, font_size=20, font_color='black', node_color='lightblue', edge_color='gray')

plt.title("Graph Representation")
plt.show()
