#represent graph using adjacency list

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

    def print_adjacency_list(self):
        for vertex in self.adj_list:
            print(vertex, "-->", ", ".join(map(str, self.adj_list[vertex])))

# Create a graph instance
graph = Graph()

# Add edges to the graph
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 0)

# Print the adjacency list
graph.print_adjacency_list()
