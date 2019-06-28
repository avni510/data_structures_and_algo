from src.queues.queue import Queue

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

    def __str__(self):
        return self.data

class Graph:
    # discovered - occurs first time we visit it
    # processed - occurs when all the children of vertex
    # have been discovered
    # parent - for an edge v1 to v2, the parent is 
    # v1 and child is v2
    # undiscovered - when a vertex has not be discovered

    def __init__(self):
        self.vertices = {}
        self.discovered = {}
        self.processed = {}
        self.parent = {}

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

    # explores all the nodes at the current depth 
    # before moving to the next depth
    # easiest to think about bfs in terms of a tree
    # good to use for determing the shortest path
    def bfs(self, start):
        self.__init_search()
        self.discovered[start] = True

        search_queue = Queue()
        search_queue.enqueue(start)

        vertex_data = []
        
        while not search_queue.is_empty():
            current_vert = search_queue.dequeue()
            vertex_data.append(current_vert.data)
            for vert in current_vert.get_connections():
                if not self.discovered[vert]:
                    self.discovered[vert] = True
                    self.parent[vert] = current_vert
                    search_queue.enqueue(vert)
            self.processed[current_vert] = True

        return vertex_data
    
    def get_vertices(self):
        return list(self.vertices.keys())

    def __init_search(self):
        for data, vertex in self.vertices.items():
            self.discovered[vertex] = False
            self.processed[vertex] = False
            self.parent[vertex] = None
