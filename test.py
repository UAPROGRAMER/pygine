import pygine
import pygame

SCR_W = 150
SCR_H = 150

FPS = 60

pygame.init()

display = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

screen = pygine.nodes.Screen(SCR_W, SCR_H, display, pygine.WHITE,
                             [pygine.nodes.Node(50, 50, [pygine.nodes.Sprite(0,0,pygame.image.load("Test64.png"),0,1,1)])],
                             True)

keys = pygine.Keys()

run = True
while run:
    screen.drawCall()
    pygame.display.flip()

    keys.update()
    screen.processCall(keys)

    if pygame.QUIT in keys.just_pressed:
        run = False
        break

    pygine.CLOCK.tick(FPS)

pygame.quit()
raise SystemExit()