# This is the Ball class originally created for MyPong.
# This class defines a ball that rebounds off the sides of a play area.

import table, random

class Ball:
    #### constructor
    def __init__(self, table, width=14, height=14, colour="red", x_speed=6, y_speed=4, x_start=0, y_start=0):
        self.width = width
        self.height = height
        self.x_posn = x_start
        self.y_posn = y_start
        self.colour = colour

        self.x_start = x_start
        self.y_start = y_start
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.table = table
        self.circle = self.table.draw_oval(self)       
    
    #### methods    
    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start
        
    def start_ball(self, x_speed, y_speed):
        self.x_speed = -x_speed if random.randint(0,1) else x_speed
        self.y_speed = -y_speed if random.randint(0,1) else y_speed
        self.start_position()
        
    def move_next(self):
        self.x_posn = self.x_posn + self.x_speed
        self.y_posn = self.y_posn + self.y_speed
        # if the ball hits the left wall:
        if(self.x_posn <= 3):
            self.x_posn = 3
            self.x_speed = -self.x_speed
        # if it hits right wall:
        if(self.x_posn >= (self.table.width - (self.width - 3))):
            self.x_posn = (self.table.width - (self.width - 3))
            self.x_speed = -self.x_speed
        # if the ball hits hits the top wall:
        if(self.y_posn <= 3):
            self.y_posn = 3
            self.y_speed = -self.y_speed
        # if it hits bottom wall:
        if(self.y_posn >= (self.table.height - (self.height - 3))):
            self.y_posn = (self.table.height - (self.height - 3))
            self.y_speed = -self.y_speed
        # finally move the circle:
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.circle, x1, y1, x2, y2)
        
    def stop_ball(self):
        self.x_speed = 0
        self.y_speed = 0
