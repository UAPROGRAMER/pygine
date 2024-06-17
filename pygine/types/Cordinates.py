from pygine.types.Vector import Vector

# cordinates class
class Cordinates():
    # pos
    x:float=0
    y:float=0

    def __init__(self, x:float, y:float) -> None:
        self.x, self.y = x, y
    
    # get tuple from Cords (x, y)
    def tuple(self) -> tuple:
        return (self.x, self.y)
    
    # move a Vector
    def move(self, vector:Vector) -> None:
        self.x += vector.x
        self.y += vector.y

# 2 Cords to a Vector
def pointsToVector(pos1:Cordinates, pos2:Cordinates) -> Vector:
    return Vector(pos2.x-pos1.x, pos2.y-pos1.y)