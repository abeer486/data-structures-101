# Graphs include nodes and edges
# Nodes are the points in the graph
# Edges are the lines connecting the nodes
# Graphs can be directed or undirected
# Directed graphs have edges with a direction
# Undirected graphs have edges without a direction
# Graphs can be weighted or unweighted
# Weighted graphs have edges with weights
# Unweighted graphs have edges without weights
# Graphs can be cyclic or acyclic
# Cyclic graphs have cycles
# Acyclic graphs do not have cycles


class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed
    
    def add_vertex(self, vertex):
        if not isinstance(vertex, str):
            raise ValueError("Vertex must be a string")
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, src, dest, weight=1):
        if src not in self.graph:
            self.add_vertex(src)
        if dest not in self.graph:
            self.add_vertex(dest)
        self.graph[src].append((dest, weight))  # Store edge as a tuple (destination, weight)
        if not self.directed:
            self.graph[dest].append((src, weight))  # Add reverse edge for undirected graphs
    
    def remove_edge(self, src, dest):
        if src in self.graph:
            self.graph[src] = [edge for edge in self.graph[src] if edge[0] != dest]
        if not self.directed and dest in self.graph:
            self.graph[dest] = [edge for edge in self.graph[dest] if edge[0] != src]
    
    def remove_vertex(self, vertex):
        if vertex in self.graph:
            # Remove any edges from other vertices to this one
            for adj in list(self.graph):
                self.graph[adj] = [edge for edge in self.graph[adj] if edge[0] != vertex]
            # Remove the vertex entry
            del self.graph[vertex]
    
    def get_adjacent_vertices(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return []
    
    def __str__(self):
        return str(self.graph)

# Example usage:
g = Graph(directed=True)
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_edge('A', 'B', 5)  # Add edge with weight 5
g.add_edge('A', 'C', 3)  # Add edge with weight 3
g.add_edge('B', 'D', 2)  # Add edge with weight 2
g.remove_vertex('F')
print(g)