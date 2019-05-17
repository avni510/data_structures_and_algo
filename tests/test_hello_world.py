import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/src")

from hello_world import HelloWorld

def test_hello_world():
    hello_world = HelloWorld()
    assert hello_world.hello() == 2
