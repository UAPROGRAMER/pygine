import pygame
import math
from pygine.types import Keys
from pygine.consts import *

class Node:
    pass

# screen class, root for the game
class Screen:
    def __init__(self, width:float, height:float, display:pygame.display.set_mode, backgroundColor:tuple[int, int, int] = WHITE,
                 children:list[Node] = [], borders:bool = True) -> None:
        self.width, self.height = width, height
        self.children = children
        self.display = display
        self.backgroundColor = backgroundColor
        self.borders = borders
        self._initCall()

    # returns smallest roporion + offset
    def getProportionAndOffset(self, screenWidth:int, screenHight:int) -> float:
        widthProportion = screenWidth/self.width
        heightProportion = screenHight/self.height
        proportion = widthProportion if widthProportion < heightProportion else heightProportion
        offset = ((screenWidth-math.ceil(self.width*proportion))/2, (screenHight-math.ceil(self.height*proportion))/2)
        return offset, proportion
    
    # draw call : calls all draw calls of children
    def drawCall(self):
        self.display.fill(self.backgroundColor)

        offset, proportion = self.getProportionAndOffset(self.display.get_width(), self.display.get_height())

        for child in self.children:
            child.drawCall(self.display, offset, proportion)

        if self.borders:
            pygame.draw.rect(self.display, BLACK, pygame.rect.Rect(0,0,self.display.get_width(), offset[1]))
            pygame.draw.rect(self.display, BLACK, pygame.rect.Rect(0,0,offset[0], self.display.get_height()))
            pygame.draw.rect(self.display, BLACK, pygame.rect.Rect(0,self.display.get_height()-offset[1],self.display.get_width(), offset[1]+1))
            pygame.draw.rect(self.display, BLACK, pygame.rect.Rect(self.display.get_width()-offset[0],0, offset[0]+1, self.display.get_height()))
    
    # process call : calls all process calls of children
    def processCall(self, keys:Keys):
        for child in self.children:
            child.processCall(keys)
    
    def _initCall(self):
        for child in self.children:
            child._initCall(self)
 
# basic node
class Node:
    _parent:Screen|Node=None
    _type:str = "node"

    def __init__(self, x:float, y:float, children:list = [], paused:bool = True, visible:bool = True) -> None:
        self.x, self.y = x, y
        self.paused = paused
        self.visible = visible
        self.children = children
    
    # process
    def process(self, keys:Keys):
        pass
    
    # draw call : calls all draw calls of children
    def drawCall(self, display, parentPosition:tuple[float,float], proportion:float):
        if self.visible:
            self.draw(display, parentPosition, proportion)
        for child in self.children:
            child.drawCall(display, (self.x*proportion+parentPosition[0], self.y*proportion+parentPosition[1]), proportion)
    
    # process call : calls all process calls of children
    def processCall(self, keys:Keys):
        if not self.paused:
            self.process(keys)
        for child in self.children:
            child.processCall(keys)
    
    def _initCall(self, parent):
        self._parent = parent
        for child in self.children:
            child._initCall(parent)

    # draw
    def draw(self, display, parentPosition:tuple[float, float], proportion:float):
        pygame.draw.circle(display, RED, (self.x*proportion+parentPosition[0], self.y*proportion+parentPosition[1]), 2*proportion)

class Rect(Node):
    _type:str = "rect"

    def __init__(self, x: float, y: float, width:float, height:float, color:tuple[int, int, int] = (0,0,255), children: list = [],
                 paused: bool = True, visible: bool = True) -> None:
        super().__init__(x, y, children, paused, visible)
        self.width = width
        self.height = height
        self.color = color

    def draw(self, display, parentPosition: tuple[float, float], proportion: float):
        rect = pygame.rect.Rect((self.x*proportion)+parentPosition[0], (self.y*proportion)+parentPosition[1], self.width*proportion, self.height*proportion)
        pygame.draw.rect(display, self.color, rect)

class Sprite(Node):
    _type:str = "sprite"

    def __init__(self, x: float, y: float, texture:pygame.Surface, rotation:float, scaleWidth:float = 1, scaleHeight:float = 1, children: list = [], paused: bool = True, visible: bool = True) -> None:
        super().__init__(x, y, children, paused, visible)
        self.texture:pygame.Surface = texture.convert_alpha()
        self.rotation = rotation
        self.scaleWidth = scaleWidth
        self.scaleHeight = scaleHeight
        self.rect = self.texture.get_rect()
        self.image = self.getImage()
            
    def getImage(self):
        image = self.texture
        if self.scaleWidth != 1 or self.scaleHeight != 1:
            image = pygame.transform.scale(image, (self.rect.width*self.scaleWidth, self.rect.height*self.scaleHeight))
        if self.rotation != 0:
            image = pygame.transform.rotate(image, self.rotation)
        return image
    
    def draw(self, display, parentPosition: tuple[float, float], proportion: float):
        image = self.image
        image = pygame.transform.scale_by(image, proportion)
        display.blit(image, ((self.x*proportion)+parentPosition[0], (self.y*proportion)+parentPosition[1]))

class Control(Rect):
    _type:str = "control"

    def __init__(self, x: float, y: float, width: float, height: float, color: tuple[int, int, int] = (0, 0, 255), colideLayer:int = 0,
                 children: list = [], paused: bool = True, visible: bool = True) -> None:
        super().__init__(x, y, width, height, color, children, paused, visible)
        self.colideLayer = colideLayer
        self.rect = pygame.rect.Rect(0,0,0,0)
    
    def draw(self, display, parentPosition: tuple[float, float], proportion: float):
        self.rect:pygame.Rect = pygame.rect.Rect((self.x*proportion)+parentPosition[0], (self.y*proportion)+parentPosition[1], self.width*proportion, self.height*proportion)
        pygame.draw.rect(display, self.color, self.rect)
    
    def process(self, keys: Keys):
        pass

    def colide(self, nodes):
        for node in nodes:
            if node._type == "control" and node.colideLayer == self.colideLayer:
                if self.rect.colliderect(node):
                    return True
        return False

    def mouseOn(self):
        mousePos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mousePos[0], mousePos[1])
        