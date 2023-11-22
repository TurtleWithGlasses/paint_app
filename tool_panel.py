import customtkinter as ctk
from settings import *

class ToolPanel(ctk.CTkToplevel):
    def __init__(self,parent,brush_float):
        super().__init__()
        self.geometry("200x300")
        self.title("Tool Panel")
        self.resizable(False,False)
        self.attributes("-topmost", True)
        self.protocol("WM_DELETE_WINDOW", self.close_app)
        self.parent = parent

        # layout
        self.columnconfigure((0,1,2),weight=1,uniform="a")
        self.rowconfigure(0,weight=2,uniform="a")
        self.rowconfigure(1,weight=3,uniform="a")
        self.rowconfigure((2,3),weight=3,uniform="a")

        BrushSizeSlider(self,brush_float)

    def close_app(self):
        self.parent.quit()

class BrushSizeSlider(ctk.CTkFrame):
    def __init__(self,parent,brush_float):
        super().__init__(parent)
        self.grid(row=2,column=0,columnspan=3,sticky="nsew",padx=5,pady=5)
        ctk.CTkSlider(self,variable=brush_float,from_=0.2,to=1).pack(fill="x",expand=True,padx=5)