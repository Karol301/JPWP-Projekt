from collections import defaultdict

class CreatingGraph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, from_verted, to_veretx, weight):
        self.adjacency_list[from_verted].append((to_veretx, weight))
    
    def get_graph(self):
        return self.adjacency_list
