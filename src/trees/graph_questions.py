from src.queues.queue import Queue
from src.trees.graph import Vertex

# connected component - maximal set of vertices such that
# there is a path between every pair of vertices
# ex: tribes in remotes part of the world

# find all the connected components, and all the nodes
# in each connected component

def connected_components(g):
    components = {}
    last_component = 1
    discovered = []

    for v in g.get_vertices_values():
        if v.data not in discovered:
            visited = bfs_components(g, v, [])
            components[last_component] = visited
            last_component += 1
            discovered += visited
    return components
            
def bfs_components(g, root_vertex, visited):
    search_queue = Queue()
    search_queue.enqueue(root_vertex)
    visited.append(root_vertex.data)

    while not search_queue.is_empty():
        curr_vertex = search_queue.dequeue()
        for v in curr_vertex.get_connections():
            if v.data not in visited:
                visited.append(v.data)
                search_queue.enqueue(v)

    return visited

# Two coloring graphs - label each vertex of a graph such
# that no edge links any two vertices of the same colo
# A graph is bipartit if it can be colored without conflicts
# while using only two colors

def is_two_colors(g):
    colored = {}
    discovered = {}
    processed = {}

    init_two_colors(g, colored, discovered, processed)

    for vert in g.get_vertices_values():
        if not discovered[vert]:
            colored[vert] = "white"
            if not bfs_colors(vert, discovered, colored, processed):
                return False

    return True

def init_two_colors(g, colored, discovered, processed):
    for v in g.get_vertices_values():
        colored[v] = "uncolored"
        discovered[v] = False 
        processed[v] = False

def bfs_colors(root, discovered, colored, processed):
    search_queue = Queue()
    search_queue.enqueue(root)

    while not search_queue.is_empty():
        curr_vertex = search_queue.dequeue()
        for v in curr_vertex.get_connections():
            if not processed[v]:
                if not is_matching_color(curr_vertex, v, colored):
                    return False
            if not discovered[v]:
                discovered[v] = True
                search_queue.enqueue(v)
        processed[v] = True

    return True
            
def is_matching_color(v1, v2, colored):
    if colored[v1] == colored[v2]:
        return False
    else:
        colored[v2] = complement(colored[v1])
        return True


def complement(color):
    if color == "white":
        return "black"
    elif color == "black":
        return "white"


# 4.1 Route Between Nodes: Given a directed graph, 
# design an algorithm to find out whether there 
# is a route between two nodes.

def is_route(g, v1, v2):
    discovered = [] 
    search_queue = Queue()

    discovered.append(v1)
    search_queue.enqueue(v1)

    while not search_queue.is_empty():
        curr_vertex = search_queue.dequeue()
        
        for vertex in curr_vertex.get_connections():
            if vertex not in discovered:
                if vertex.data == v2.data:
                    return True
                else:
                    discovered.append(vertex)
                    search_queue.enqueue(vertex)
    return False
