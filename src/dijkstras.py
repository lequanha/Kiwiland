class Dijkstras:
    """This class implements Dijkstra's algorithm to store all of the shortest paths and distances from every node to all reachable nodes."""

    """
    'shortest_distances' is a dictionary storing the shortest distances between any two nodes.
    'shortest_paths' is a dictionary storing the shortest routes (node names) between any two nodes.
    """

    """The __init__ method finds and stores all shortest routes for the graph."""
    def __init__(self, graph_dictionary):
        self.shortest_distances = {}
        self.shortest_paths = {}
        
        # Call Dijkstra's algorithm with every node to be the start node.
        for start_node in graph_dictionary.keys():
            self.shortest_distances[start_node], self.shortest_paths[start_node] = self.calculate_shortest_routes(graph_dictionary, start_node)


    """The calculate_shortest_routes method uses Dijkstra's algorithm to compute all shortest routes."""
    def calculate_shortest_routes(self, graph_dictionary, start_node):     
        shortest_routes = {}
        visit_nodes = {start_node: 0}
        previous_nodes = {}
        
        while visit_nodes:
            next_node_key = min(visit_nodes, key=visit_nodes.get)
            distance_to_next_node = visit_nodes.pop(next_node_key)

            for node_key, node_value in graph_dictionary[next_node_key].items():
                if node_key not in shortest_routes:
                    addup_edges = distance_to_next_node + node_value
                    if node_key not in visit_nodes:
                        visit_nodes[node_key] = addup_edges
                        previous_nodes[node_key] = next_node_key
                    else:
                        if (visit_nodes[node_key] > addup_edges):
                            visit_nodes[node_key] = addup_edges
                            previous_nodes[node_key] = next_node_key

            # We cannot assign start node done with a zero distance
            if next_node_key != start_node or distance_to_next_node > 0:
                shortest_routes[next_node_key] = distance_to_next_node
        return shortest_routes, previous_nodes

    """The get_distance method returns the shortest distance from a start node to an end node."""
    def get_distance(self, start_node, end_node):
        if end_node in self.shortest_distances.get(start_node, {}):
            """Print routes"""
            routes = end_node
            node_key = end_node
            while (self.shortest_paths[start_node][node_key] != start_node): 
                routes = routes + self.shortest_paths[start_node][node_key]
                node_key = self.shortest_paths[start_node][node_key]
            routes = routes + start_node
            routes = routes[::-1]
            print("\nThe shortest route from " + start_node + " to " + end_node + " is: " + routes + " with distance " + str(self.shortest_distances[start_node][end_node]))
            
            return self.shortest_distances[start_node][end_node]

        print("\nNO SUCH ROUTE from " + start_node + " to " + end_node)
        return "NO SUCH ROUTE"

