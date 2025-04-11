import tkinter as tk
from DrawingGraph import DrawingGraph

class App:
    def __init__(self, master, graph):
        
        self.master = master

        self.graph = graph

        # Frame to hold matplotlib canvas
        graph_frame = tk.Frame(master)
        graph_frame.pack()

        self.draw = DrawingGraph(self.graph, graph_frame)

        self.entry = tk.Entry(master)            # For node name
        self.entry.pack()
        self.edges_entry = tk.Entry(master)       # For comma-separated connections
        self.edges_entry.pack()

        add_btn = tk.Button(master, text="Add Node", command=self.add_vertex)
        add_btn.pack()
        del_btn = tk.Button(master, text="Delete Node", command=self.del_vertex)
        del_btn.pack()

        self.displayGraph()


    def displayGraph(self):
        self.draw.draw()

    
    def add_vertex(self):
        node = self.entry.get().strip()
        edges = []
        if self.edges_entry.get():
            edges = self.edges_entry.get().split(',')
        self.graph.add_vertex(node)
        
        for edge in edges:
            edge = edge.strip()
            if edge == node:
                print('Niepoprawnie wprowadzone wierzchołki')
                return
            if edge not in self.graph.adjacency_list:
                self.graph.adjacency_list[edge] = []
        
        for edge in edges:
            self.graph.add_edge(node, edge, 1)
        
        self.displayGraph()
    
    def del_vertex(self):
        print('papapaf')
        
