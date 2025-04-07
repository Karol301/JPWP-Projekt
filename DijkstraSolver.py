import heapq

class DijkstraSolver:
    def __init__(self, graph):
        self.graph = graph
    
    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.graph.adjacency_list}
        previous = {vertex: None for vertex in self.graph.adjacency_list}
        distances[start] = 0

        priority_queue = []
        heapq.heappush(priority_queue, (0, start))

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph.adjacency_list[current_vertex]:
                new_distance = distances[current_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        return distances, previous
    
    def shortest_path(self, start, end):
        distances, previous = self.dijkstra(start)
        if distances[end] == float('inf'):
            return None

        path = []
        current = end
        while current is not None:
            path.insert(0, current)
            current = previous[current]

        return path, distances[end]
