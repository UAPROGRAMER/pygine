import pygame

CLOCK = pygame.time.Clock()

WHITE:tuple[int, int, int] = (255, 255, 255)
BLACK:tuple[int, int, int] = (0, 0, 0)
RED:tuple[int, int, int] = (255, 0, 0)
BLUE:tuple[int, int, int] = (0, 0, 255)
GREEN:tuple[int, int, int] = (0, 255, 0)
YELLOW:tuple[int, int, int] = (255, 255, 0)
SKY:tuple[int, int, int] = (0, 255, 255)
PINK:tuple[int, int, int] = (255, 0, 255)

hexToDec : dict = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'a':10,
    'b':11,
    'c':12,
    'd':13,
    'e':14,
    'f':15
}

def hexColor(hex:str) -> tuple[int, int, int]:
    if len(hex) != 7:
        raise ValueError("Bad hex string.")
    
    hex = hex[1:]

    color = [0,0,0]
    color[0] = hexToDec[hex[0]]*16+hexToDec[hex[1]]
    color[1] = hexToDec[hex[2]]*16+hexToDec[hex[3]]
    color[2] = hexToDec[hex[4]]*16+hexToDec[hex[5]]

    return (color[0], color[1], color[2])