#undirected graph using adjacency list - using detect_cycle() - detect cycle in the graph list

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)  # Directed edge: u -> v

    def detect_cycle(self):
        visited = set()
        rec_stack = set()

        def dfs(vertex):
            visited.add(vertex)
            rec_stack.add(vertex)

            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True

            rec_stack.remove(vertex)
            return False

        for node in self.adj_list:
            if node not in visited:
                if dfs(node):
                    return True
        return False

# Create a graph instance
graph = Graph()

# Add edges to the graph
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 3)  # Self-loop to create a cycle

# Detect and print cycle information
if graph.detect_cycle():
    print("Cycle Detected:", True)
else:
    print("Cycle Detected:", False)
