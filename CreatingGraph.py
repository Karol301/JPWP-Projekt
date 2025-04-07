from collections import defaultdict

class CreatingGraph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_verted, to_veretx, weight):
        self.graph[from_verted].append((to_veretx, weight))
    
    def get_graph(self):
        return self.graph

graph = CreatingGraph()
while True:
    vertex = input("Podaj nazwę wierzchołka: ")
    if vertex == "end":
        break
    graph.add_vertex(vertex)

    while True:
        to_vertex = input(f"Z jakim wierzchołkiem połączony jest wierzchołek '{vertex}'? ")
        if to_vertex == "end":
            break
        else:
            weight = input(f"Podaj wagę między '{vertex}' a '{to_vertex}': ")
            graph.add_edge(vertex, to_vertex, weight)
        

print(graph.get_graph())