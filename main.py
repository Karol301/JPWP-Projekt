from DijkstraSolver import DijkstraSolver
from CreatingGraph import CreatingGraph
from App import App
import tkinter as tk

graph = CreatingGraph()
solve = DijkstraSolver(graph)

root = tk.Tk()
app = App(root, graph)
root.mainloop()