# src/traffic_graph.py

class TrafficGraph:
    def __init__(self):
        self.graph = {}

    def add_intersection(self, node):
        """Add an intersection (node) to the graph"""
        if node not in self.graph:
            self.graph[node] = []

    def add_road(self, node1, node2, weight):
        """Add a road (edge) between two intersections with a weight (e.g., congestion level)"""
        if node1 not in self.graph:
            self.add_intersection(node1)
        if node2 not in self.graph:
            self.add_intersection(node2)
        self.graph[node1].append((node2, weight))
        self.graph[node2].append((node1, weight))  # If it's a two-way road

    def get_intersections(self):
        """Return all intersections (nodes)"""
        return self.graph.keys()

    def get_roads(self, node):
        """Return all roads (edges) from an intersection"""
        return self.graph.get(node, [])
