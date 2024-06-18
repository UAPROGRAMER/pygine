# Pygine

## Pygine in python and pygame module that helps create games on pygame quickly.

This module conteins a number of tools to help create your game on a pygame. Pygine uses classes to create objects that can interact with each other. <br/>
In module all elements divided to 3 groups:
* [Types](#types)
* [Nodes](#nodes)
* [Engine](#engine)

## Types

Types is elements used by nodes and engine. They are necessary for any game. <br/>
Types contains:
* Cordinates
* Vector
* Keys
* Debugtools

### Cordinates():

Type that used for cordinates of an object.

#### Variables:

##### x:float = 0

##### y:float = 0

#### Functions:

##### init(self, x:float, y:float) -> None:

self.x, self.y = x, y

##### tuple(self) -> tuple:

return (self.x, self.y)

##### move(self, vector:Vector) -> None:

self.x += vector.x
self.y += vector.y

## Nodes

Nodes is a building blocks for your game. This classes can be extended for your needs or you can just use default Nodes. <br/>
List of default Nodes:
* [Node](#node)

### Node():

Basic Node.

#### Variables:

##### cordinates:Cordinates = Cordinates(0,0)

##### paused:bool = True

##### visible:bool = True

##### nodetype:str = "node"

#### Functions:

##### init(self, cordinates:Cordinates, paused:bool = True, visible:bool = True) -> None:

self.cordinates = cordinates
self.paused = paused
self.visible = visible

##### process(self, nodes, keys:Keys) -> None:

pass

##### draw(self, display) -> None:

pygame.draw.circle(display, (0,0,0), self.cordinates.tuple(), 2)

## Engine

Engine is a heart of your program. To create a game you first create an Engine and then start a mainloop function. <br/>

### Functions:

#### init(self, displaySize:tuple = (0,0), fps:int = 60, title:str = "Pygine", bgcolor:pygame.Color = (255, 255, 255), nodes:list = [], debugtools:list = [], bgimage:str = None, icon:str = None, fullscreen:bool = False) -> None:

Intializes Engine and pygame.

#### mainloop(self) -> None:

Mainloop is a function that runs a loop until game is closed. This function do all work at processing and drawing Nodes. <br/>
Mainloop runs tasks in this sequence:
* Cheking events (like exit)
* Updating Keys
* Processing Nodes
* Drawing everything
* Updating display

#### draw_fps(self) -> None:

Only for debug.
