from enum import Enum
from pygine.types.Cordinates import Cordinates

class Anchor(Enum):
    none = "none"
    top = "top"
    bottom = "bottom"
    right = "right"
    left = "left"
    topright = "topright"
    topleft = "topleft"
    bottomright = "bottomright"
    bottomleft = "bottomleft"
    center = "center"

    def getCordinates(anchor:str, width:int, height:int) -> Cordinates:
        match anchor:
            case "top":
                return Cordinates(width/2, 0)
            case "bottom":
                return Cordinates(width/2, height)
            case "right":
                return Cordinates(width, height/2)
            case "left":
                return Cordinates(0, height/2)
            case "topright":
                return Cordinates(width, 0)
            case "topleft":
                return Cordinates(0, 0)
            case "bottomright":
                return Cordinates(width, height)
            case "bottomleft":
                return Cordinates(0, height)
            case "center":
                return Cordinates(width/2, height/2)
            case _:
                raise ValueError("Wrong anchor argument.")