import networkx as nx
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class DrawingGraph:
    def __init__(self, graph, parent_frame):
        self.graph = graph
        self.pos = {}

        self.figure = Figure(figsize=(10, 6), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.figure.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        self.canvas = FigureCanvasTkAgg(self.figure, master=parent_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def draw(self):
        self.ax.clear()

        self.ax.set_xlim([-1.2, 1.2])
        self.ax.set_ylim([-1.2, 1.2])
        
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_axis_off()

        G = nx.Graph()

        for node in self.graph.get_vertices():
            G.add_node(node)

        for u, v, w in self.graph.get_edges():
            G.add_edge(u, v, weight=w)

        self.pos = nx.circular_layout(G)

        nx.draw(
            G,
            pos=self.pos,
            with_labels=True,
            ax=self.ax,
            node_color='skyblue',
            edge_color='gray',
            node_size=1500,
            font_size=16
        )

        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(
            G,
            pos=self.pos,
            edge_labels=edge_labels,
            ax=self.ax,
            label_pos=0.6,
            font_size=12,
            font_color='black',
            rotate=False
        )

        self.canvas.draw()

        