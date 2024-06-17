import pygine as pg

displaySize = (500, 500)
fps = 60
title = "test"
bgcolor = (255, 255, 255)
nodes = [pg.Node(pg.Cordinates(250,250))]
debugtools = [pg.Debugtools.fps]

engine = pg.Engine(displaySize, fps, title, bgcolor, nodes,
                   debugtools, None, None, False)
engine.mainloop()