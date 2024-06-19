from enum import Enum

class RectSizeModes(Enum):
    px = "px"
    perc = "perc"

class RectSize():
    xmode = None
    x:float
    ymode = None
    y:float

    def __init__(self, x:float, y:float, xmode=RectSizeModes.px, ymode=RectSizeModes.px) -> None:
        self.x, self.y, self.xmode, self.ymode = x, y, xmode, ymode
    
    def getSize(self, width:float, height:float) -> list:
        ret = [0,0]
        if self.xmode == RectSizeModes.px:
            ret[0] = self.x
        elif self.xmode == RectSizeModes.perc:
            ret[0] = width*(self.x/100)
        if self.ymode == RectSizeModes.px:
            ret[1] = self.y
        elif self.ymode == RectSizeModes.perc:
            ret[1] = height*(self.y/100)
        return ret