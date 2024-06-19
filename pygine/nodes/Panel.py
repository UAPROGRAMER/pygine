import pygame
from pygine.types.Cordinates import Cordinates
from pygine.types.Keys import Keys
from pygine.nodes.Node import Node
from pygine.types.Anchor import Anchor
from pygine.types.Vector import *
from pygine.types.RectSize import RectSize, RectSizeModes

# Node/Panel for ui
class Panel(Node):
    #cordinates:Cordinates = Cordinates(0,0)    # cordinates
    #paused:bool = True                   # is node paused
    #visible:bool = True                  # is node visible
    nodetype:str = "panel"               # node type
    color:pygame.Color = (0,0,0)
    anchor:Anchor = Anchor.none
    offset:Vector = Vector(0,0)
    rectSize:RectSize

    def __init__(self, cordinates: Cordinates, rectSize:RectSize, color:pygame.Color = (0,0,0),
                 anchor:Anchor=Anchor.none, offset:Vector = Vector(0,0), paused: bool = True, visible: bool = True) -> None:
        super().__init__(cordinates, paused, visible)
        self.cordinates.move(offset)
        self.color = color
        self.anchor = anchor
        self.offset = offset
        self.rectSize = rectSize
    
    #def process(self, nodes, keys: Keys) -> None:
    #    pass

    def draw(self, display) -> None:
        if self.anchor != Anchor.none:
            self.cordinates = Anchor.getCordinates(self.anchor.value, display.get_width(), display.get_height())
            self.cordinates.move(self.offset)
        size = self.rectSize.getSize(display.get_width(), display.get_height())
        rect = pygame.Rect(self.cordinates.x, self.cordinates.y, size[0], size[1])
        pygame.draw.rect(display, self.color, rect)