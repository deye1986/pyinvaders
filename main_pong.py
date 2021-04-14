from tkinter import *
import table, ball, bat

#initialse globals
x_velocity = 16
y_velocity = 16
score_left = 0
score_right = 0
first_serve = True

#order a window from tkinter
window = Tk()
window.title('PongTwo - David Ikin 2020 - github.com/deye1986 ')

#order a table from the table.py file
my_table = table.Table(window, net_colour='Green', vertical_net=True)

#order a ball from ball.py file
my_ball = ball.Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity, width=24, height=24, colour='MediumPurple4', x_start=288, y_start=188)

#order bats
bat_L = bat.Bat(table=my_table, width=15, height=100, x_posn=20, y_posn=150, colour='blue')
bat_R = bat.Bat(table=my_table, width=15, height=100, x_posn=575, y_posn=150, colour='HotPink')


def game_flow():
    global first_serve
    global score_left
    global score_right

    # wait for the first serve:
    if(first_serve == True):
        my_ball.stop_ball()
        first_serve = False

    #detect if ball colides with the bats
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)

    #detect if ball has hit left wall
    if(my_ball.x_posn <=3):
        my_ball.stop_ball()
        score_left =+ 1
        my_table.draw_score(score_left, score_right)
        my_ball.start_position()
        bat_L.start_position()
        bat_R.start_position()
        my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
        my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)

    #detect if ball has hit right wall:
    my_ball.move_next()
    window.after(50, game_flow)
    if(my_ball.x_posn + my_ball.width >= my_table.width - 3):
        my_ball.stop_ball()
        score_right =+ 1
        my_table.draw_score(score_left, score_right)
        my_ball.start_position()
        bat_L.start_position()
        bat_R.start_position()
        my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
        my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)

def restart_game(master):
    global score_left
    global score_right
    my_ball.start_ball(x_speed=x_velocity, y_speed=0)
    if(score_left == 'W' or score_left == 'L'):
        score_left = 0
        score_right = 0
    my_table.draw_score(score_left, score_right)
    
#controls, keyboard
window.bind('a', bat_L.move_up)
window.bind('z', bat_L.move_down)
window.bind('k', bat_R.move_up)
window.bind('m', bat_R.move_down)
window.bind('A', bat_L.move_up)
window.bind('Z', bat_L.move_down)
window.bind('K', bat_R.move_up)
window.bind('M', bat_R.move_down)
window.bind('<space>', restart_game)

#call the game_flow loop
game_flow()

#start the tkinter loop process
window.mainloop()

