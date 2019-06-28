import pytest

from src.trees.graph_questions import *
from src.trees.graph import Graph

def test_is_route_returns_true():
    g = Graph()
    
    for i in range(1, 7):
        g.add_vertex(i)

    g.add_edge(1, 2)
    g.add_edge(1, 5)
    g.add_edge(1, 6)
    g.add_edge(2, 5)
    g.add_edge(2, 3)
    g.add_edge(5, 4)
    g.add_edge(3, 4)
   
    v1 = g.get_vertex(1)
    v2 = g.get_vertex(3)
    assert is_route(g, v1, v2)
    
def test_is_route_returns_false():
    g = Graph()
    
    for i in range(1, 7):
        g.add_vertex(i)

    g.add_edge(1, 2)
    g.add_edge(1, 5)
    g.add_edge(1, 6)
    g.add_edge(2, 5)
    g.add_edge(2, 3)
    g.add_edge(5, 4)
    g.add_edge(3, 4)

    v1 = g.get_vertex(6)
    v2 = Vertex(7)
    assert not is_route(g, v1, v2)
    
