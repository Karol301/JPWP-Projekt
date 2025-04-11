from DijkstraSolver import DijkstraSolver
from CreatingGraph import CreatingGraph
from App import App
import tkinter as tk

graph = CreatingGraph()
solve = DijkstraSolver(graph)

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
            weight = int(input(f"Podaj wagę między '{vertex}' a '{to_vertex}': "))
            graph.add_edge(vertex, to_vertex, weight)

start_vertex = input("Podaj wierzchołek startowy: ")
end_vertex = input("Podaj wierzchołek końcowy: ")
if start_vertex == end_vertex:
    print("Wierzchołki są takie same")

result = solve.shortest_path(start_vertex, end_vertex)
path, cost = result

print(f"Najkrótsza ścieżka z {start_vertex} do {end_vertex}: {' -> '.join(path)} (koszt: {cost})")
root = tk.Tk()
app = App(root, graph)
root.mainloop()