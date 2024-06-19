import pygine as pg

displaySize = (500, 500)
fps = 60
title = "test"
bgcolor = (255, 255, 255)
nodes = [pg.Panel(pg.Cordinates(0,0), pg.RectSize(5, 5, pg.RectSizeModes.perc, pg.RectSizeModes.perc), anchor=pg.Anchor.center, offset=pg.Vector(-25,-25))]
debugtools = [pg.Debugtools.fps]

engine = pg.Engine(displaySize, fps, title, bgcolor, nodes,
                   debugtools, None, None, False, True)
engine.mainloop()