#graph adjacency list-DFS

from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        traversal_order = []

        while queue:
            vertex = queue.popleft()
            traversal_order.append(vertex)

            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print("BFS Traversal Order:", traversal_order)

# Create a graph instance
graph = Graph()

# Add edges to the graph
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 0)

# Perform BFS starting from vertex 0
graph.bfs(0)
