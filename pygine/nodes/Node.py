import pygame
from pygine.types.Cordinates import Cordinates
from pygine.types.Keys import Keys

# class Node the base of all nodes
class Node():

    cordinates = Cordinates(0,0)    # cordinates
    paused = True                   # is node paused
    visible = True                  # is node visible
    nodetype = "node"               # node type

    def __init__(self, cordinates:Cordinates, paused:bool = True, visible:bool = True) -> None:
        self.cordinates = cordinates
        self.paused = paused
        self.visible = visible
    
    # process func get called every frame
    def process(self, nodes, keys:Keys):
        pass
    
    # draws node
    def draw(self, display):
        pygame.draw.circle(display, (0,0,0), self.cordinates.tuple(), 2)