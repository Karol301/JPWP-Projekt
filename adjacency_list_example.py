from collections import defaultdict

adjacency_list = defaultdict(list)

def add_edge(u, v):
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

def add_edge(u, v, weight):
    adjacency_list[u].append((v, weight))
    adjacency_list[v].append((u, weight))

add_edge('A', 'B', 2)
add_edge('A', 'C', 5)
add_edge('B', 'D', 3)

print(adjacency_list)

adjacency_list = [
    [1, 2, 3],   # sąsiedzi wierzchołka 0
    [0, 2],      # sąsiedzi wierzchołka 1
    [0, 1],
    [0]
]

adjacency_list = {
    'A': ['B', 'C', 'D'],   # sąsiedzi wierzchołka A
    'B': ['A', 'C'],        # sąsiedzi wierzchołka B
    'C': ['A', 'B'],
    'D': ['A']
}