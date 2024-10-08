# src/main.py

from traffic_graph import TrafficGraph
from traffic_congestion import TrafficCongestionManager

def main():
    # Initialize the traffic graph and congestion manager
    traffic = TrafficGraph()
    congestion_manager = TrafficCongestionManager()

    # Add intersections
    traffic.add_intersection("A")
    traffic.add_intersection("B")
    traffic.add_intersection("C")

    # Add roads with congestion level
    traffic.add_road("A", "B", 5)  # Road from A to B with congestion level 5
    traffic.add_road("B", "C", 3)  # Road from B to C with congestion level 3
    traffic.add_road("A", "C", 7)  # Road from A to C with congestion level 7

    # Simulate congestion management
    congestion_manager.add_road(5, "Road A-B")
    congestion_manager.add_road(3, "Road B-C")
    congestion_manager.add_road(7, "Road A-C")
    
    # Process roads based on congestion
    congestion_manager.process_roads()

if __name__ == "__main__":
    main()
