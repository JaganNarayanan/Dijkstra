# References:
# 1. https://www.geeksforgeeks.org/graph-and-its-representations/
# 2. https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs

# An implementation of a weighted, directed graph as an adjacency list. This
# means that it's represented as a map from each node to a list of it's
# respective adjacent nodes.
class Graph:
    def __init__(self):
        # DO NOT EDIT THIS CONSTRUCTOR
        self.graph = {}

    def add_edge(self, node1, node2, weight):
        # Adds a directed edge from `node1` to `node2` to the graph with weight defined by `weight`.

        # If an edge btwn node1 and node2 already exists in the graph, don't do anything:
        if self.has_edge(node1, node2):
            return
        # Check if node1 already exists in the graph:
        if node1 not in self.graph:
            # If node1 does not exist, create node1 with node2 as the neighbor with the associated weight, (x,y)
            self.graph[node1] = [(node2, weight)]
        else:
            # If node1 does exist, add node2 as a neighbor with the associated weight, (x, y)
            self.graph[node1].append((node2, weight))

    def has_edge(self, node1, node2):
        # Returns whether the graph contains an edge from `node1` to `node2`.
        if node1 not in self.graph:
            return False
        return node2 in [x for (x, i) in self.graph[node1]]

    def get_neighbors(self, node):
        # Returns the neighbors of `node` as a list of tuples [(x, y), ...] where
        # `x` is the neighbor node, and `y` is the weight of the edge from `node`
        # to `x`.

        # Check if node exists in graph:
        if node not in self.graph:
            # if node does not exist, return empty list
            return []
        else:
            # If node exists in graph, return its neighbors:
            return self.graph[node]
