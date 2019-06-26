class Vertex:
    def __init__(self, data):
        self.data = data
        self.connected_to = {}

    def add_neighbor(self, data, weight = 0):
        self.connected_to[data] = weight

    def get_connections(self):
        return list(self.connected_to.keys())

    def get_weight(self, neighbor):
        return self.connected_to[neighbor]

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, data):
        new_vertex = Vertex(data)
        self.vertices[data] =  new_vertex
        return new_vertex

    def add_edge(self, v1, v2, weight=0):
        if v1 not in self.vertices:
            self.vertices[v1] = Vertex(v1)
        if v2 not in self.vertices:
            self.vertices[v2] = Vertex(v2)
        self.vertices[v1].add_neighbor(self.vertices[v2])
        self.vertices[v2].add_neighbor(self.vertices[v1])

    def get_vertex(self, data):
        return self.vertices[data]
