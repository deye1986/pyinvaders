# This is the Table class originally created for MyPong.
# This class defines a Table that is a 2D rectangle that is a play area.

from tkinter import *

class Table:
    #### constructor
    def __init__(self, window, colour="black", net_colour="green",
                 width=600, height=400, vertical_net=False, horizontal_net=False):
        self.width = width
        self.height = height
        self.colour = colour
        
        # order a canvas to draw on from tkinter's Canvas class:
        self.canvas = Canvas(window, bg=self.colour, height=self.height, width=self.width)
        self.canvas.pack()

        # add a net to the canvas using its create_line method:
        if(vertical_net):
            self.canvas.create_line(self.width/2, 0, self.width/2, self.height, width=2, fill=net_colour, dash=(15, 23))
        if(horizontal_net):
            self.canvas.create_line(0, self.height/2, self.width, self.height/2, width=2, fill=net_colour, dash=(15, 23))

        # add scoreboard:
        font = ("monaco", 72)
        self.scoreboard = self.canvas.create_text(300, 65, font=font, fill = "darkgreen")

    #### methods
    # extra tool for adding a rectangle to the canvas
    def draw_rectangle(self, rectangle):
        x1 = rectangle.x_posn
        x2 = rectangle.x_posn + rectangle.width
        y1 = rectangle.y_posn
        y2 = rectangle.y_posn + rectangle.height
        c = rectangle.colour
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=c)

    # extra tool for adding an oval to the canvas
    def draw_oval(self, oval):
        x1 = oval.x_posn
        x2 = oval.x_posn + oval.width
        y1 = oval.y_posn
        y2 = oval.y_posn + oval.height
        c = oval.colour
        return self.canvas.create_oval(x1, y1, x2, y2, fill=c)
    
    # extra tools for manipulating items on the canvas:
    def move_item(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)
    
    def remove_item(self, item):
        self.canvas.delete(item)

    def change_item_colour(self, item, c):
        self.canvas.itemconfigure(item, fill=c)

    # extra tool for adding score to the canvas:
    def draw_score(self, left, right):
        scores = str(right) + "  " + str(left)
        self.canvas.itemconfigure(self.scoreboard, text=scores)

    
