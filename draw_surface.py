from tkinter import Canvas
from settings import *

class DrawSurface(Canvas):
    def __init__(self,parent, color_string, brush_float):
        super().__init__(parent,background=CANVS_BG,
                         bd=0,
                         highlightthickness=0,
                         relief="ridge")
        self.pack(expand=True,fill="both")

        self.color_string = color_string
        self.brush_float = brush_float
        self.allow_draw = False

        self.bind("<Motion>", self.draw)
        self.bind("<Button>", self.activate_draw)
        self.bind("<ButtonRelease>", self.deactivate_draw)
    
    def draw(self,event):
        if self.allow_draw:
            self.create_line(event.x - 5,
                             event.y - 5,
                             event.x + 5,
                             event.y + 5,
                             fill="black")

    def activate_draw(self,event):
        self.allow_draw = True

    def deactivate_draw(self,event):
        self.allow_draw = False