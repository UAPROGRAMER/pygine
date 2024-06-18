import pygame
from pygine.types.Cordinates import Cordinates
from pygine.types.Keys import Keys
from pygine.nodes.Node import Node
from pygine.types.Anchor import Anchor
from pygine.types.Vector import *

# Node/Panel for ui
class Panel(Node):
    #cordinates:Cordinates = Cordinates(0,0)    # cordinates
    #paused:bool = True                   # is node paused
    #visible:bool = True                  # is node visible
    nodetype:str = "panel"               # node type
    rect:pygame.Rect = None
    color:pygame.Color = (0,0,0)
    anchor:Anchor = Anchor.none
    offset:Vector = Vector(0,0)
    percents:bool = False
    percentsrect:Cordinates = Cordinates(0,0)
    vector:Vector = Vector(0,0)

    def __init__(self, cordinates: Cordinates, vector:Vector, color:pygame.Color = (0,0,0), anchor:Anchor=Anchor.none, offset:Vector = Vector(0,0),
                 percents:bool = False, percentsrect:Cordinates = Cordinates(0,0), paused: bool = True, visible: bool = True) -> None:
        super().__init__(cordinates, paused, visible)
        self.vector = vector
        self.rect = pygame.Rect(self.cordinates.x, self.cordinates.y, vector.x, vector.y)
        self.color = color
        self.anchor = anchor
        self.offset = offset
        self.percents = percents
        self.percentsrect = percentsrect
    
    #def process(self, nodes, keys: Keys) -> None:
    #    pass

    def draw(self, display) -> None:
        if self.anchor != Anchor.none:
            self.cordinates = Anchor.getCordinates(self.anchor.value, display.get_width(), display.get_height())
            self.cordinates.move(self.offset)
            self.rect = pygame.Rect(self.cordinates.x, self.cordinates.y, self.vector.x, self.vector.y)
        if self.percents:
            self.rect = pygame.Rect(self.cordinates.x, self.cordinates.y, display.get_width()*self.percentsrect.x,
                                    display.get_height()*self.percentsrect.y)
        pygame.draw.rect(display, self.color, self.rect)