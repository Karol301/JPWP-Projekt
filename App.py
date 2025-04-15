import tkinter as tk
from tkinter import ttk
from DrawingGraph import DrawingGraph
from DijkstraSolver import DijkstraSolver

class App:
    def __init__(self, master, graph):
        self.master = master
        self.graph = graph
        self.solver = DijkstraSolver(graph)

        master.title("Interaktywny Graf")
        master.geometry("1100x650")
        master.configure(padx=10, pady=10)

        # Konfiguracja siatki
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # === GRAF ===
        graph_frame = tk.Frame(master, bd=2, relief=tk.SUNKEN)
        graph_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.draw = DrawingGraph(self.graph, graph_frame)

        # === PANEL DOLNY ===
        form_frame = tk.Frame(master)
        form_frame.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        form_frame.columnconfigure(0, weight=1)
        form_frame.columnconfigure(1, weight=1)

        # === LEWA STRONA – DODAWANIE/USUWANIE ===
        left_frame = tk.LabelFrame(form_frame, text="Dodawanie / Usuwanie wierzchołków", padx=10, pady=10)
        left_frame.grid(row=0, column=0, sticky="w", padx=(0, 20))

        tk.Label(left_frame, text="Dodaj wierzchołek:").grid(row=0, column=0, sticky='w')
        self.vertex_entry = tk.Entry(left_frame, width=10)
        self.vertex_entry.grid(row=0, column=1, padx=5)

        tk.Label(left_frame, text="Połączony z:").grid(row=0, column=2, sticky='w')
        self.edges_entry = tk.Entry(left_frame, width=15)
        self.edges_entry.grid(row=0, column=3, padx=5)

        tk.Label(left_frame, text="Waga:").grid(row=0, column=4, sticky='w')
        self.weight_entry = tk.Entry(left_frame, width=5)
        self.weight_entry.grid(row=0, column=5, padx=5)
        self.weight_entry.insert(0, "1")

        add_btn = tk.Button(left_frame, text="➕ Dodaj", command=self.add_vertex, width=10)
        add_btn.grid(row=0, column=6, padx=10)

        # Usuwanie wierzchołka
        tk.Label(left_frame, text="Usuń wierzchołek:").grid(row=1, column=0, sticky='w', pady=(10, 0))
        self.delete_entry = tk.Entry(left_frame, width=15)
        self.delete_entry.grid(row=1, column=1, padx=5, pady=(10, 0))

        del_btn = tk.Button(left_frame, text="🗑️ Usuń", command=self.del_vertex, width=10)
        del_btn.grid(row=1, column=2, padx=10, pady=(10, 0))

        # === PRAWA STRONA – DIJKSTRA ===
        right_frame = tk.LabelFrame(form_frame, text="Najkrótsza ścieżka (Dijkstra)", padx=10, pady=10)
        right_frame.grid(row=0, column=1, sticky="e")

        tk.Label(right_frame, text="Początek:").grid(row=0, column=0)
        self.start_entry = tk.Entry(right_frame, width=10)
        self.start_entry.grid(row=0, column=1, padx=5)

        tk.Label(right_frame, text="Koniec:").grid(row=0, column=2)
        self.end_entry = tk.Entry(right_frame, width=10)
        self.end_entry.grid(row=0, column=3, padx=5)

        path_btn = tk.Button(right_frame, text="🧭 Oblicz ścieżkę", command=self.calc_path)
        path_btn.grid(row=0, column=4, padx=10)

        self.path_label = tk.Label(right_frame, text="", fg="green", font=("Arial", 10, "italic"))
        self.path_label.grid(row=1, column=0, columnspan=5, pady=(10, 0))

        # Wyświetl pierwszy rysunek grafu
        self.displayGraph()

    def displayGraph(self):
        self.draw.draw()

    def add_vertex(self):
        node = self.vertex_entry.get().strip()
        if ',' in node or node == "":
            self.path_label.config(text='Wprowadź tylko jeden wierzchołek', fg='red')
            return

        edges = self.edges_entry.get().split(',') if self.edges_entry.get() else []
        weight = self.weight_entry.get().strip()

        try:
            weight = float(weight)
        except ValueError:
            self.path_label.config(text='Waga musi być liczbą', fg='red')
            return

        self.graph.add_vertex(node)

        for edge in edges:
            edge = edge.strip()
            if edge == node or edge == "":
                self.path_label.config(text='Niepoprawnie wprowadzone wierzchołki', fg='red')
                return
            if edge not in self.graph.adjacency_list:
                self.path_label.config(text=f'Wierzchołek "{edge}" nie istnieje', fg='red')
                return

        for edge in edges:
            self.graph.add_edge(node, edge.strip(), weight)

        self.displayGraph()
        self.path_label.config(text="Dodano wierzchołek i krawędzie.", fg="green")

    def del_vertex(self):
        nodes_to_delete = self.delete_entry.get().split(',')
        for node in nodes_to_delete:
            self.graph.delete_vertex(node.strip())
        self.displayGraph()
        self.path_label.config(text="Usunięto wierzchołek(i).", fg="green")

    def calc_path(self):
        start = self.start_entry.get().strip()
        end = self.end_entry.get().strip()

        if not start or not end:
            self.path_label.config(text="Uzupełnij pola początek i koniec.", fg='red')
            return

        if start == end:
            self.path_label.config(text="Wierzchołki są takie same", fg='red')
            return

        try:
            path, cost = self.solver.shortest_path(start, end)
            if not path:
                self.path_label.config(text=f"Brak ścieżki między {start} a {end}.", fg='red')
            else:
                path_str = " → ".join(path)
                self.path_label.config(text=f"Ścieżka: {path_str}  (koszt: {cost})", fg='green')
        except Exception as e:
            self.path_label.config(text=f"Błąd: {e}", fg='red')
