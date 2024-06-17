from math import sqrt

# Vector class
class Vector():
    x:float=0
    y:float=0

    def __init__(self, x:float, y:float) -> None:
        self.x, self.y = x, y
    
    # get Vector length
    def length(self) -> float:
        return sqrt((self.x**2)+(self.y**2))
    
    # get this vector bunt normalized
    def normalized(self):
        length = self.length()
        return Vector(self.x/length, self.y/length)

    # get tuple of this Vector (x, y)
    def tuple(self) -> tuple:
        return (self.x, self.y)

    # add to this vector another
    def add(self, vector) -> None:
        self.x += vector.x
        self.y += vector.y
    
    # multiply this vector
    def multiply(self, num:int) -> None:
        self.x *= num
        self.y *= num
    
    # get Vector (0,0)
    def zero():
        return Vector(0,0)

# get sum of Vectors
def sumVectors(vectors:list[Vector]=[]) -> Vector:
    retVector = Vector(0,0)

    for vector in vectors:
        retVector.add(vector)
    
    return retVector

# subtract 2 Vectors
def subVectors(vector1:Vector, vector2:Vector) -> Vector:
    return Vector(vector1.x-vector2.x, vector1.y-vector2.y)