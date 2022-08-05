from pyglet.shapes import Rectangle
import pyglet


class ProcessBar(Rectangle):
    """docstring for ProcessBar"""
    batch = None
    def __init__(self,x,y,width,height,color,batch,name):
        super().__init__(x,y,width,height,color,batch)
        self.batch = batch
        self.name  = name
    