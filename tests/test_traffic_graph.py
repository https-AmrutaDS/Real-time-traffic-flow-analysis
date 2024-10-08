# tests/test_traffic_graph.py

import unittest
from src.traffic_graph import TrafficGraph

class TestTrafficGraph(unittest.TestCase):

    def test_add_intersection(self):
        graph = TrafficGraph()
        graph.add_intersection("A")
        self.assertIn("A", graph.get_intersections())

    def test_add_road(self):
        graph = TrafficGraph()
        graph.add_road("A", "B", 5)
        self.assertIn(("B", 5), graph.get_roads("A"))

if __name__ == '__main__':
    unittest.main()
