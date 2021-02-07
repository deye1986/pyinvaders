# This is the main file for MyInvaders.

from tkinter import *
import table, ball, bat, random


window = Tk()
window.title("MyInvaders")
my_table = table.Table(window)

# add background image
starry_night_image = PhotoImage(file = "stars.gif")
my_table.canvas.create_image(0, 0, anchor=NW, image = starry_night_image, tags="bg_img")

# move the image to bottom of image stack (so the scoreboard can be seen above the background)
# by moving any canvas objects tagged as "bg_img" to the back using the lower() method
my_table.canvas.lower("bg_img")

# initialise global variables
x_velocity = 0
y_velocity = -10
first_serve=True
direction = "right"

# order a missile from the ball class
my_ball = ball.Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity,
                    height=15, width=8, colour="black")

# order a defender from the bat class
bat_B = bat.Bat(table=my_table, width=50, height=30,
                x_posn=250, y_posn=350, colour="blue")

# order invaders from the bat class and start them moving to the right
invaders = []
rows=0
gap=30
colour = ("green", "orange", "yellow", "purple")
while rows < 5:
    n=1
    while n < 7:
        i=80
        invader = bat.Bat(table=my_table, width=50, height=20, x_speed=3, y_speed=15,
                          x_posn=(n*i), y_posn=25+(rows*gap), colour=colour[(rows-1) %4])
        invaders.append(invader)
        n = n+1
    rows = rows+1

#### Functions:        
def game_flow():
    global first_serve
    global direction
    game_over = False
    # wait for first serve:
    if(first_serve == True):
        my_ball.stop_ball()
        first_serve = False

    # detect if missile has hit an invader:
    for b in invaders:
        if(b.detect_collision(my_ball, sides_sweet_spot=False) != None):
            my_table.remove_item(b.rectangle)                
            invaders.remove(b)
            hide_missile()
            
        if(len(invaders) == 0):
            my_table.remove_item(my_ball.circle)
            my_table.canvas.itemconfigure(my_table.scoreboard, text="YOU WIN")
            
    # detect if missile hit the top wall:
    if(my_ball.y_posn <= 3):
        hide_missile()
        first_serve=True
    
    my_ball.move_next()

    # handle movement of invaders
    directionChange = False;
    for b in invaders:
        directionChange = directionChange or move_brick_next(b, direction)
        game_over = detect_game_over(b, bat_B.y_posn)
    if(game_over):
        my_ball.stop_ball()
        for b in invaders:
            b.x_speed=0
            b.y_speed=0
        my_table.canvas.itemconfigure(my_table.scoreboard, text="GAME OVER")
    if(directionChange):
        for b in invaders:
            b.move_down(b)
        if(direction == "right"):
            direction = "left"
        else:
            direction = "right"
    window.after(50, game_flow)
    
def restart_game(master):
    first_serve=False
    my_ball.start_ball(0,0)
    my_ball.x_speed=x_velocity
    my_ball.y_speed=y_velocity
    my_table.change_item_colour(my_ball.circle, "red")
    my_ball.x_posn = (bat_B.x_posn + bat_B.width/2)
    my_ball.y_posn = bat_B.y_posn

# Moves invaders to left or right and looks to see if they should be moved down
# returns true if direction must change
def move_brick_next(brick, direction):
    if(direction == "left"):
        brick.move_left(brick)
        if(brick.x_posn < 10):  # if the brick reaches the left wall
            return True
        else:
            return False
    else:
        brick.move_right(brick)
        if((brick.x_posn + brick.width) > my_table.width-10):  # if the brick reaches the right wall
            return True
        else:
            return False

# detect if invaders reach the bottom
def detect_game_over(invader, bottom):
    if((invader.y_posn + invader.height) > bottom):
        return True
    else:
        return False

# hide missile
def hide_missile():
    my_ball.stop_ball()
    my_ball.x_posn=0
    my_ball.y_posn=my_table.height-my_ball.height
    my_table.change_item_colour(my_ball.circle, "black")

# bind the controls of the bat to keys on the keyboard
window.bind("<Left>", bat_B.move_left)
window.bind("<Right>", bat_B.move_right)

# bind restart to spacebar
window.bind("<space>", restart_game)

game_flow()
window.mainloop()
