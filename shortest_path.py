# References:
# 1. https://www.pythonpool.com/dijkstras-algorithm-python/
# 2. http://nmamano.com/blog/dijkstra/dijkstra.html
# 3. https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
# 4. http://semanticgeek.com/graph/exploring-dijkstras-shortest-path-algorithm/


def shortest_path(graph, source, target):
    # `graph` is an object that provides a get_neighbors(node) method that returns
    # a list of (node, weight) edges. both of your graph implementations should be
    # valid inputs. you may assume that the input graph is connected, and that all
    # edges in the graph have positive edge weights.
    #
    # `source` and `target` are both nodes in the input graph. you may assume that
    # at least one path exists from the source node to the target node.
    #
    # this method should return a tuple that looks like
    # ([`source`, ..., `target`], `length`), where the first element is a list of
    # nodes representing the shortest path from the source to the target (in
    # order) and the second element is the length of that path

    # To keep track of the shortest paths to reach each node with a dict of the form dict[node] = shortest path
    shortest_paths = {source: 0}
    # To keep track of all the nodes visited
    visited = []
    # To keep track of the previous node visited
    previous_node = {}

    while target not in visited:
        # Keeping track of nodes that need to be visited
        unvisited = {}
        for node in shortest_paths:
            if node not in visited:
                unvisited[node] = shortest_paths[node]

        # In the case that there is no shortest path, return message
        if not unvisited:
            return "No Possible Solution"

        # Select the node among the unvisited notes with the shortest path as the current node
        current_node = min(unvisited.items(), key=lambda x: x[1])[0]
        current_node_weight = shortest_paths[current_node]
        # Get neighbors of the current node (using get_neighbors meethod from the previous question)
        neighbors = graph.get_neighbors(current_node)

        # If neighbors are not null:
        if neighbors:
            for n in neighbors:

                neighbor = n[0]
                neighbor_weight = n[1]

                new_weight = neighbor_weight + current_node_weight

                if neighbor not in shortest_paths:
                    shortest_paths[neighbor] = new_weight
                    previous_node[neighbor] = current_node

                else:
                    prior_weight = shortest_paths[neighbor]
                    # If the new weight is less than the prior documented weight, then update the weight
                    if new_weight < prior_weight:
                        shortest_paths[neighbor] = new_weight
                        previous_node[neighbor] = current_node

        # Keeping track of the visited nodes:
        visited.append(current_node)

    # To find the nodes traversed in the shortest path:
    # Start with the target node and add it to the path
    start = target
    path = [target]
    while previous_node[start] != source:
        # Look up the value of the start variable and add it to the path
        path.append(previous_node[start])
        # path.insert(0, previous_node[start])
        # Use the value of the start variable as the new key
        start = previous_node[start]
    # Add source node
    path.append(source)
    # Reverse the order of the path (from backward to forward)
    path.reverse()

    # Find shortest path length between the start and target nodes:
    length = shortest_paths[target]

    return (path, length)

