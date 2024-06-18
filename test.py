import pygine as pg

displaySize = (500, 500)
fps = 60
title = "test"
bgcolor = (255, 255, 255)
nodes = [pg.Panel(pg.Cordinates(0,0), pg.Vector(50,50), (0,0,0), pg.Anchor.top, pg.Vector(0,0), True, pg.Cordinates(0.2,0.2))]
debugtools = [pg.Debugtools.fps]

engine = pg.Engine(displaySize, fps, title, bgcolor, nodes,
                   debugtools, None, None, False, True)
engine.mainloop()