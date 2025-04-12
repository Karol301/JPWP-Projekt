import tkinter as tk
from DrawingGraph import DrawingGraph

class App:
    def __init__(self, master, graph):
        
        self.master = master

        self.graph = graph

        # Frame to hold matplotlib canvas
        graph_frame = tk.Frame(master)
        graph_frame.pack()

        form_frame = tk.Frame(master)
        form_frame.pack()

        self.draw = DrawingGraph(self.graph, graph_frame)


        tk.Label(form_frame, text="Dodaj wierzchołek:").grid(row=0, column=0, sticky='w')
        self.vertex_entry = tk.Entry(form_frame)
        self.vertex_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="Połączony z:").grid(row=1, column=0, sticky='w')
        self.edges_entry = tk.Entry(form_frame)
        self.edges_entry.grid(row=1, column=1)

        add_btn = tk.Button(form_frame, text="Dodaj", command=self.add_vertex)
        add_btn.grid(row=2, column=0)
        
        tk.Label(form_frame, text="Usuń wierzhołek:").grid(row=0, column=2, sticky='w')
        self.delete_entry = tk.Entry(form_frame)
        self.delete_entry.grid(row=0, column=3)
        
        del_btn = tk.Button(form_frame, text="Usuń", command=self.del_vertex)
        del_btn.grid(row=1, column=2)

        tk.Label(form_frame, text="Najkrótsza ścieżka").grid(row=0, column=4)
        tk.Label(form_frame, text="Początek:").grid(row=1, column=4, sticky='w')
        self.start_entry = tk.Entry(form_frame)
        self.start_entry.grid(row=1, column=5)

        tk.Label(form_frame, text="Koniec:").grid(row=2, column=4, sticky='w')
        self.end_entry = tk.Entry(form_frame)
        self.end_entry.grid(row=2, column=5)

        self.displayGraph()


    def displayGraph(self):
        self.draw.draw()

    
    def add_vertex(self):
        if len(self.vertex_entry.get().split(',')) > 1:
            print('Wprowadź tylko jeden wierzchołek')
            return
        node = self.vertex_entry.get().strip()
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
                # self.graph.adjacency_list[edge] = []
                print('Co najmniej jeden z wierzchołków nie jest stworzony')
                return
        
        for edge in edges:
            self.graph.add_edge(node, edge, 1)
        
        self.displayGraph()
    
    def del_vertex(self):
        nodes_to_delete = self.delete_entry.get().split(',')
        for node in nodes_to_delete:
            self.graph.delete_vertex(node)
        
        self.displayGraph()