import networkx as nx
import matplotlib.pyplot as plt
from CreatingGraph import CreatingGraph

class DrawingGraph:
    def __init__(self, graph):
        self.graph = graph
    
    def draw(self):
        G = nx.Graph()
        edges = self.graph.get_edges()

        for i in edges:
            G.add_nodes_from(i[0])
            G.add_edges_from([(i[0], i[1])])
            G.add_edge(i[0], i[1], weight=i[2])
        
        nx.draw(G, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1500, font_size=16)

        plt.show()
