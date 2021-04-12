# An implementation of a weighted, directed graph as an edge list. This means
# that it's represented as a list of tuples, with each tuple representing an
# edge in the graph.
class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, node1, node2, weight):
        # Adds a directed edge from `node1` to `node2` to the graph with weight
        # defined by `weight`.

        # Check if directed edge already exists in the graph:
        if not self.has_edge(node1, node2):
            # If directed edge does not exist, create edge with (node1, node2, weight)
            self.graph.append((node1, node2, weight))

    def has_edge(self, node1, node2):
        # Returns whether the graph contains an edge from `node1` to `node2`.
        return (node1, node2) in [(x, y) for (x, y, z) in self.graph]

    def get_neighbors(self, node):
        # Returns the neighbors of `node` as a list of tuples [(x, y), ...] where
        # `x` is the neighbor node, and `y` is the weight of the edge from `node`
        # to `x`.

        neighbors = []
        # Go through all the edges in the graph
        for edge in self.graph:
            # Check if the node, z, we are looking for is present in the edge, (z, x, y):
            if edge[0] == node:
                # If node is found in the graph, add every neighbor with associated weight, (x,y), to the resulting list of neighbors
                neighbors.append((edge[1], edge[2]))
                # If node is not found, return empty list
        return neighbors

