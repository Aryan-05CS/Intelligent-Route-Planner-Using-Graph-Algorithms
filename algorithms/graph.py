class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):

        self.graph.setdefault(u, []).append((v, weight))
        self.graph.setdefault(v, []).append((u, weight))