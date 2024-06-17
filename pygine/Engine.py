import pygame
from pygine.types.Debugtools import Debugtools
from pygine.types.Keys import Keys

class Engine():

    display = None                          # pygame display
    displaySize:tuple = (0,0)               # display size in tuple
    title:str = "Pygine"                    # display title
    fps:int = 60                            # frames per second
    clock = pygame.time.Clock()             # clock
    bgcolor:pygame.Color = (255, 255, 255)  # background color
    nodes:list = []                         # list of nodes
    basicFont = None                        # basic font
    debugtools:list[Debugtools] = []        # debug tools
    keys:Keys = Keys()                      # keys
    bgimage = None                          # backgroung image (optional)
    icon = None                             # icon (optional)

    # setting up engine
    def __init__(self, displaySize:tuple = (0,0), fps:int = 60, title:str = "Pygine",
                 bgcolor:pygame.Color = (255, 255, 255), nodes:list = [],
                 debugtools:list = [], bgimage:str = None, icon:str = None,
                 fullscreen:bool = False) -> None:
        
        # initializing pygame
        pygame.init()

        self.displaySize = displaySize

        if fullscreen:
            self.display = pygame.display.set_mode(self.displaySize, pygame.FULLSCREEN)
        else:
            self.display = pygame.display.set_mode(self.displaySize)
        
        self.title = title
        pygame.display.set_caption(self.title)

        if icon:
            pygame.display.set_icon(pygame.image.load(icon))
        
        self.fps = fps
        self.bgcolor = bgcolor
        self.nodes = nodes
        self.basicFont = pygame.font.SysFont(None, 30)
        self.debugtools = debugtools

        if bgimage:
            self.background_image = pygame.image.load(bgimage).convert()
    
    # main game loop
    def mainloop(self) -> None:
        run = True

        while run:

            # saving all events into a variable
            events = pygame.event.get()

            # cheking all events
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
            
            # updating keys
            self.keys.update(events)

            # processing nodes if not paused
            for node in self.nodes:
                if node.paused == False:
                    node.process(self.nodes, self.keys)
            
            # drawing background
            self.display.fill(self.bgcolor)
            if self.bgimage:
                self.display.blit(self.bgimage, (0,0))

            # drawing nodes if visible
            for node in self.nodes:
                if node.visible == True:
                    node.draw(self.display)
            
            # debug things
            if Debugtools.fps in self.debugtools:
                self.draw_fps()
            if Debugtools.nodes in self.debugtools:
                print(self.nodes)

            # updating display
            pygame.display.update()

            # this thing do fps (magic)
            self.clock.tick(self.fps)
        
        # exiting pygame when done
        pygame.quit()
    
    # func for drawing debug fps
    def draw_fps(self) -> None:
        fps = str(int(self.clock.get_fps()))
        fps_text = self.basicFont.render(fps, True, pygame.Color('black'))
        self.display.blit(fps_text, (10, 10))