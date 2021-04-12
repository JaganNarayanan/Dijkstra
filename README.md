# Dijkstra

This repo illustrates an implementation of Dijkstra’s Shortest-Path Algorithm to find the shortest path in any given graph.

First, a directed graph is implemented in two ways:
1. Adjacency list (see graph_adjacency_list.py) where a graph is represented as a map, where the keys are nodes in the graph and the values are a list of all the nodes adjacent to the key node. 
2. Edge list (see graph_edge_list.py )where a graph is represented as a list of tuples, where each tuple represents an edge between two nodes.

Then, Dijkstra’s Shortest-Path Algorithm (see shortest_path.py) is implemented such that regardless of the type of graphs given as input (adjacency list or edge list), the shortest path will be returned as a tuple that looks like ([‘start_node‘, ..., ‘target_node‘], ‘length‘) where the first part is the shortest path from the ‘source_node‘ to the ‘target_node‘ and the second part is the ‘length‘ of said path.

Test cases for two types of graphs (see graph_test.py) and the shortest path algorithm (shortest_path_test.py) have also been included. 





