import networkx as nx
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DrawingGraph:
    def __init__(self, graph, parent_frame):
        self.graph = graph
        self.pos = {}

        self.figure = Figure(figsize=(10, 5))
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=parent_frame)
        self.canvas.get_tk_widget().pack()
    
    def draw(self):
        self.ax.clear()

        G = nx.Graph()

        for node in self.graph.get_vertices():
            G.add_node(node)

        for u, v, w in self.graph.get_edges():
            G.add_edge(u, v, weight=w)

        self.pos = nx.random_layout(G)

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

        