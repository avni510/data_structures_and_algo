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

def test_connected_components():
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

    for i in range(7, 10):
        g.add_vertex(i)

    g.add_edge(7, 8)
    g.add_edge(8, 9)
    
    result = connected_components(g)

    assert sorted(result[1]) == [1, 2, 3, 4, 5, 6]
    assert sorted(result[2]) == [7, 8, 9]

def test_is_two_colors_returns_false():
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
    
    assert not is_two_colors(g) 

def test_is_two_colors_returns_true():
    g = Graph()
    
    for i in range(1, 7):
        g.add_vertex(i)

    g.add_edge(1, 2)
    g.add_edge(1, 6)
    g.add_edge(2, 5)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 1)

    assert is_two_colors(g)
