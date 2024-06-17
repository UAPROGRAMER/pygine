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

## Nodes

Nodes is a building blocks for your game. This classes can be extended for your needs or you can just use default Nodes. <br/>
List of default Nodes:
* Node

## Engine

Engine is a heart of your program. To create a game you first create an Engine and then start a mainloop function. <br/>
Engine includes this functions:
* init
* mainloop
* draw_fps

### Init
Intializes Engine and pygame.

### Mainloop
Mainloop is a function that runs a loop until game is closed. This function do all work at processing and drawing Nodes. <br/>
Mainloop runs tasks in this sequence:
* Cheking events (like exit)
* Updating Keys
* Processing Nodes
* Drawing everything
* Updating display
