import customtkinter as ctk
from settings import *

class ToolPanel(ctk.CTkToplevel):
    def __init__(self,parent,brush_float,color_string):
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


        ColorSliderPanel(self,color_string)
        BrushSizeSlider(self,brush_float)
        ColorPanel(self,color_string)

    def close_app(self):
        self.parent.quit()

class ColorSliderPanel(ctk.CTkFrame):
    def __init__(self,parent,color_string):
        super().__init__(parent)
        self.grid(row=0,column=0,sticky="nsew",padx=5,pady=5)

        # data
        self.color_string = color_string
        self.r_int = ctk.IntVar(value=self.color_string.get()[0])
        self.g_int = ctk.IntVar(value=self.color_string.get()[1])
        self.b_int = ctk.IntVar(value=self.color_string.get()[2])
        self.color_string.trace("w",self.set_color)

        self.rowconfigure((0,1,2),weight=1, uniform="a")
        self.columnconfigure(0,weight=1,uniform="a")

        # widgets
        ctk.CTkSlider(self,
                      command=lambda value: self.set_single_color("r",value),
                      variable=self.r_int,
                      from_=0,
                      to=15,
                      number_of_steps=16,
                      button_color=SLIDER_RED,
                      button_hover_color=SLIDER_RED).grid(column=0,row=0,padx=4)
        ctk.CTkSlider(self,
                      command=lambda value: self.set_single_color("g",value),
                      variable=self.g_int,
                      from_=0,
                      to=15,
                      number_of_steps=16,
                      button_color=SLIDER_GREEN,
                      button_hover_color=SLIDER_GREEN).grid(column=0,row=1,padx=4)
        ctk.CTkSlider(self,
                      command=lambda value: self.set_single_color("b",value),
                      variable=self.b_int,
                      from_=0,
                      to=15,
                      number_of_steps=16,
                      button_color=SLIDER_BLUE,
                      button_hover_color=SLIDER_BLUE).grid(column=0,row=2,padx=4)

    def set_single_color(self,color,value):
        current_color_list = list(self.color_string.get())

        match color:
            case "r": current_color_list[0] = COLOR_RANGE[int(value)]
            case "g": current_color_list[1] = COLOR_RANGE[int(value)]
            case "b": current_color_list[2] = COLOR_RANGE[int(value)]
        self.color_string.set(f'{"".join(current_color_list)}')

    def set_color(self,*args):
        self.r_int.set(COLOR_RANGE.index(self.color_string.get()[0]))
        self.g_int.set(COLOR_RANGE.index(self.color_string.get()[1]))
        self.b_int.set(COLOR_RANGE.index(self.color_string.get()[2]))

class ColorPanel(ctk.CTkFrame):
    def __init__(self,parent,color_string):
        super().__init__(parent,fg_color="transparent")
        self.grid(row=1,column=0,columnspan=3,padx=5,pady=6)
        self.color_string = color_string

        # layout
        self.rowconfigure([row for row in range(COLOR_ROWS)],weight=1,uniform="a")
        self.columnconfigure([column for column in range(COLOR_COLS)],weight=1,uniform="a")

        # widgets
        for row in range(COLOR_ROWS):
            for col in range(COLOR_COLS):
                color = COLORS[row][col]
                ColorFieldButton(self, row, col, color, self.pick_color)

    def pick_color(self,color):
        self.color_string.set(color)

class ColorFieldButton(ctk.CTkButton):
    def __init__(self,parent,row,col,color, pick_color):
        super().__init__(parent,
                         text="",
                         fg_color=f"#{color}",
                         hover_color=f"#{color}",
                         corner_radius=1,
                         command=self.click_handler)
        self.grid(row=row,column=col,padx=0.4,pady=0.4)

        self.pick_color = pick_color
        self.color = color
    
    def click_handler(self):
        self.pick_color(self.color)


class BrushSizeSlider(ctk.CTkFrame):
    def __init__(self,parent,brush_float):
        super().__init__(parent)
        self.grid(row=2,column=0,columnspan=3,sticky="nsew",padx=5,pady=5)
        ctk.CTkSlider(self,variable=brush_float,from_=0.2,to=1).pack(fill="x",expand=True,padx=5)