import networkx as nx
# import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# this is matplotlib embedded in Tkinter

class DrawingGraph:
    def __init__(self, graph, parent_frame):
        self.graph = graph
        # self.pos = {}

        self.figure = Figure(figsize=(5, 5))
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=parent_frame)
        self.canvas.get_tk_widget().pack()
    
    def draw(self):
        self.ax.clear()
        G = nx.Graph()
        edges = self.graph.get_edges()

        for i in edges:
            G.add_nodes_from(i[0])
            G.add_edges_from([(i[0], i[1])])
            G.add_edge(i[0], i[1], weight=i[2])
        
        # fixed_nodes = list(self.pos.keys())

        # pos = nx.spring_layout(G, pos=fixed_nodes, fixed=fixed_nodes, seed=42)
        # nx.draw(G, pos, with_labels=True, ax=self.ax, node_color='skyblue',
        #         edge_color='gray', node_size=1500, font_size=16)
        nx.draw(G, with_labels=True, ax=self.ax, node_color='skyblue',
                 edge_color='gray', node_size=1500, font_size=16)
        self.canvas.draw()
