class Graph:
    def __init__(self):
        from collections import defaultdict
        self.adj_list=defaultdict(list)

    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]=[]

    def add_edge(self,from_vertex,to_vertex):
        if from_vertex in self.adj_list and to_vertex in self.adj_list:
            self.adj_list[from_vertex].append(to_vertex)
            self.adj_list[to_vertex].append(from_vertex)


    def bfs(self,start_vertex):
        visited=set()
        queue=[start_vertex]
        visited.add(start_vertex)
        while queue:
            vertex=queue.pop(0)
            print(vertex,end=" ")
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def dfs(self,start_vertex):
        visited=set()
        stack=[start_vertex]
        while stack:
            vertex=stack.pop()
            if vertex not in visited:
                print(vertex,end=" ")
                visited.add(vertex)
                for neighbor in self.adj_list[vertex]:
                    if neighbor not  in visited:
                        stack.append(neighbor)


#Graph creation
graph=Graph()
graph.add_vertex("1")
graph.add_vertex("2")
graph.add_vertex("3")
graph.add_vertex("4")
graph.add_vertex("5")
graph.add_vertex("6")
graph.add_vertex("7")

graph.add_edge("1","2")
graph.add_edge("3","2")
graph.add_edge("2","7")
graph.add_edge("3","5")
graph.add_edge("7","5")
graph.add_edge("4","6")



print(graph.adj_list)
print()
print("BFS->")
graph.bfs("1")
print("\n")
print("DFS->")
graph.dfs("1")



import networkx as nx
import matplotlib.pyplot as plt
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
