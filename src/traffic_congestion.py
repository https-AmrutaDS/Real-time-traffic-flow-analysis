# src/traffic_congestion.py

import heapq

class TrafficCongestionManager:
    def __init__(self):
        self.congestion_queue = []

    def add_road(self, congestion_level, road_name):
        """Add road with its congestion level to the priority queue"""
        heapq.heappush(self.congestion_queue, (congestion_level, road_name))

    def process_roads(self):
        """Process roads based on congestion level (lowest first)"""
        while self.congestion_queue:
            congestion_level, road_name = heapq.heappop(self.congestion_queue)
            print(f"Processing {road_name} with congestion level {congestion_level}")
