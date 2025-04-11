from collections import defaultdict

class CreatingGraph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex == to_vertex:
            print('Niepoprawnie wprowadzone wierzchołki')
            return
        self.adjacency_list[from_vertex].append((to_vertex, weight))
        self.adjacency_list[to_vertex].append((from_vertex, weight))
    
    def get_graph(self):
        return self.adjacency_list
    
    def get_edges(self):
        edges = []
        for from_vertex, neighbors in self.adjacency_list.items():
            for to_vertex, weight in neighbors:
                edges.append((from_vertex, to_vertex, weight))
        return edges
