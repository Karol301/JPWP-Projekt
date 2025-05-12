from DijkstraSolver import DijkstraSolver
from Graph import Graph
from App import App
import tkinter as tk

graph = Graph()
solve = DijkstraSolver(graph)

root = tk.Tk()
app = App(root, graph)
root.mainloop()