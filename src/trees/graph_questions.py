from src.queues.queue import Queue
from src.trees.graph import Vertex

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

# 4.7 Build Order: You are given a list of projects and a list of dependencies 
# (which is a list of pairs of projects, where the second project 
# is dependent on the first project). All of a project's dependencies must be 
# built before the project is. Find a build order that will allow the projects 
# to be built. If there is no valid build order, return an error
