import networkx as nx
# import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# this is matplotlib embedded in Tkinter

class DrawingGraph:
    def __init__(self, graph, parent_frame):
        self.graph = graph
        # self.pos = {}

        self.figure = Figure(figsize=(10, 5))
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=parent_frame)
        self.canvas.get_tk_widget().pack()
    
    def draw(self):
        self.ax.clear()
        G = nx.Graph()
        edges = self.graph.get_edges()
        vertices = self.graph.get_vertices()

        for i in edges:
            G.add_nodes_from(i[0])
            G.add_edges_from([(i[0], i[1])])
            G.add_edge(i[0], i[1], weight=i[2])

        for i in vertices:
            G.add_node(i)
        
        # if not self.pos:
            # self.pos = nx.spring_layout(G, seed=42)
            # self.pos = nx.spectral_layout(G)
        # else:
        #     fixed_nodes = list(self.pos.keys())
        #     # self.pos = nx.spring_layout(G, pos=self.pos, fixed=fixed_nodes, seed=42)
        #     self.pos = nx.spectral_layout(G, pos=self.pos, fixed=fixed_nodes, seed=42)

        # nx.draw(G, pos=self.pos, with_labels=True, ax=self.ax, node_color='skyblue',
        #         edge_color='gray', node_size=1500, font_size=16)


        nx.draw(G, with_labels=True, ax=self.ax, node_color='skyblue',
                 edge_color='gray', node_size=1500, font_size=16)
        self.canvas.draw()
